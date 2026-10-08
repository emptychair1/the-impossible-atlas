from pathlib import Path
p=Path("index.html")
s=p.read_text()
if "function drawAverie(time,walking)" in s:
    print("Averie already installed")
    raise SystemExit(0)
needle="function loop(t){"
assert needle in s, "Game loop not found"
raven="""
// Averie: animated shoulder-perched raven.
function drawAverie(time,walking){
  const bob=Math.sin(time*.004)*1.5+(walking?Math.sin(time*.017)*2:0);
  const blink=(time%4100)<105;
  const turn=Math.sin(time*.0017)>.72;
  const wing=Math.sin(time*.0031)*1.4;
  ctx.save();
  ctx.translate(x+dir*(-39),ground-214+bob);ctx.scale(dir,1);
  ctx.fillStyle='#080b15';ctx.strokeStyle='#1c2633';ctx.lineWidth=1.7;
  ctx.beginPath();ctx.moveTo(-6,16);ctx.lineTo(-24,36);ctx.lineTo(-12,30);ctx.lineTo(-19,39);ctx.lineTo(2,23);ctx.fill();
  ctx.beginPath();ctx.ellipse(0,9,15,22,-.25,0,Math.PI*2);ctx.fill();ctx.stroke();
  ctx.fillStyle='#141c2a';ctx.beginPath();ctx.ellipse(-5+wing,14,9,17,-.3,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#080b15';ctx.beginPath();ctx.ellipse(6,-14,11,12,turn?-.2:.16,0,Math.PI*2);ctx.fill();
  ctx.beginPath();ctx.moveTo(13,-16);ctx.lineTo(26,-12);ctx.lineTo(13,-10);ctx.closePath();ctx.fill();
  ctx.fillStyle=blink?'#171b24':'#c1c5b6';ctx.beginPath();ctx.ellipse(10,-17,blink?2:2.4,blink?.5:2,0,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#080b15';ctx.fillRect(-6,25,2,6);ctx.fillRect(3,25,2,6);
  ctx.restore();
}
"""
s=s.replace(needle,raven+needle,1)
needle2="ctx.restore();requestAnimationFrame(loop)}requestAnimationFrame(loop);"
assert needle2 in s, "Render loop end not found"
s=s.replace(needle2,"drawAverie(t,!!move);"+needle2,1)
p.write_text(s)
print("Averie installed")
