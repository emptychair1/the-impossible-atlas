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
 const bob=Math.sin(t*.003)*1.1+(walking?Math.sin(t*.017)*1.5:0);
 const w=47,h=51;
 ctx.save();
 ctx.translate(x,ground);
 ctx.scale(dir,1);
 // Anchor Averie's visible feet just behind Josh's neck, on top of the shoulder.\n ctx.drawImage(averieSprite,-13,-202+bob,w,h);
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
