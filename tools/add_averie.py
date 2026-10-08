from pathlib import Path
import re
p=Path("index.html")
s=p.read_text()

# Remove the earlier placeholder raven function, if present.
s=re.sub(r"// AVERIE_APPROVED_SPRITE_V1[\s\S]*?\nfunction loop\(t\)\{", "function loop(t){", s, count=1)
s=re.sub(r"// Averie: animated shoulder-perched raven\.[\s\S]*?\nfunction loop\(t\)\{", "function loop(t){", s, count=1)
s=s.replace("drawAverie(t,!!move);", "")
data=Path("assets/averie_perched.b64").read_text().strip()
sprite_code="""
// AVERIE_APPROVED_SPRITE_V1
const averieSprite=new Image();
averieSprite.src='data:image/png;base64,"""+data+"""';
function drawAverie(t,walking){
 if(!averieSprite.complete||!averieSprite.naturalWidth)return;
 const shoulderX=[-35,-36,-35,-33,-34,-36,-35,-34];
 const shoulderY=[-190,-192,-190,-189,-191,-192,-190,-189];
 const phase=walking?frame:0;
 const footX=x+dir*shoulderX[phase];
 const footY=ground+shoulderY[phase];
 const w=47,h=51;
 ctx.save();
 ctx.translate(footX,footY);
 ctx.scale(dir,1);
 ctx.drawImage(averieSprite,-w*.40,-h*.95,w,h);
 ctx.restore();
}
"""
assert "function loop(t){" in s
s=s.replace("function loop(t){",sprite_code+"\nfunction loop(t){",1)
end="ctx.restore();requestAnimationFrame(loop)}requestAnimationFrame(loop);"
assert end in s
s=s.replace(end,"drawAverie(t,!!move);"+end,1)
p.write_text(s)
print("Installed approved Averie sprite")
