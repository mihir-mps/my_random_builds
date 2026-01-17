from flask import Flask, render_template_string

app = Flask(__name__)

data = {
    "CEO": ["Strategic Management", "System Management", "People Management"],
    "Strategic Management": ["Vision & Direction", "Strategic Thinking", "Growth Strategy", "Governance & Stewardship"],
    "Vision & Direction": ["Vision Formulation", "Vision Communication"],
    "Vision Formulation": ["Long-Term Aspiration", "Strategic Narrative"],
    "Long-Term Aspiration": ["Clear compelling future state articulated"],
    "Strategic Narrative": ["Vision translated into understandable story"],
    "Vision Communication": ["Leadership Alignment", "Organization Buy-in"],
    "Leadership Alignment": ["Top team consistently reinforces vision"],
    "Organization Buy-in": ["Employees understand strategic intent"],
    "Strategic Thinking": ["Environmental Scanning", "Strategic Choice"],
    "Environmental Scanning": ["Market Intelligence", "Competitive Analysis"],
    "Market Intelligence": ["Continuous monitoring of market forces"],
    "Competitive Analysis": ["Clear understanding of competitors moves"],
    "Strategic Choice": ["Trade-off Decisions", "Resource Prioritization"],
    "Trade-off Decisions": ["Conscious selection of what not to pursue"],
    "Resource Prioritization": ["Capital aligned to strategic priorities"],
    "Growth Strategy": ["Opportunity Identification", "Strategic Investment"],
    "Opportunity Identification": ["New Market Exploration", "Product or Service Expansion"],
    "New Market Exploration": ["Viable growth avenues identified"],
    "Product or Service Expansion": ["Portfolio aligned to demand trends"],
    "Strategic Investment": ["Inorganic Growth", "Organic Scaling"],
    "Inorganic Growth": ["Mergers or partnerships evaluated prudently"],
    "Organic Scaling": ["Core business scaled sustainably"],
    "Governance & Stewardship": ["Board Engagement", "Risk Oversight", "Ethical Leadership"],
    "Board Engagement": ["Governance Effectiveness"],
    "Governance Effectiveness": ["Board decisions add strategic value"],
    "Risk Oversight": ["Enterprise Risk View"],
    "Enterprise Risk View": ["Key risks anticipated and mitigated"],
    "Ethical Leadership": ["Values-Based Decisions"],
    "Values-Based Decisions": ["Trust and integrity institutionalized"],
    "System Management": ["Organizational Design", "Process Excellence", "Technology & Digital", "Performance Management"],
    "Organizational Design": ["Structure Design", "Operating Model"],
    "Structure Design": ["Role Clarity", "Decision Rights"],
    "Role Clarity": ["Clear accountability across functions"],
    "Decision Rights": ["Decisions made at the right level"],
    "Operating Model": ["End-to-End Flow"],
    "End-to-End Flow": ["Work moves seamlessly across units"],
    "Process Excellence": ["Process Standardization", "Process Optimization", "Continuous Improvement"],
    "Process Standardization": ["SOP Definition"],
    "SOP Definition": ["Consistent execution across organization"],
    "Process Optimization": ["Waste Elimination"],
    "Waste Elimination": ["Reduced inefficiencies and rework"],
    "Continuous Improvement": ["Feedback Loops"],
    "Feedback Loops": ["Processes refined using data"],
    "Technology & Digital": ["Digital Strategy", "System Integration", "Automation Enablement"],
    "Digital Strategy": ["Technology Roadmap"],
    "Technology Roadmap": ["IT aligned with business strategy"],
    "System Integration": ["Data Flow Integrity"],
    "Data Flow Integrity": ["Single source of truth established"],
    "Automation Enablement": ["Productivity Gains"],
    "Productivity Gains": ["Manual effort systematically reduced"],
    "Performance Management": ["KPI Framework", "Monitoring & Review", "Corrective Action"],
    "KPI Framework": ["Metric Definition"],
    "Metric Definition": ["Measures reflect strategic priorities"],
    "Monitoring & Review": ["Performance Cadence"],
    "Performance Cadence": ["Regular disciplined reviews conducted"],
    "Corrective Action": ["Course Correction"],
    "Course Correction": ["Timely interventions improve outcomes"],
    "People Management": ["Leadership Development", "Talent Management", "Culture & Values", "Employee Experience"],
    "Leadership Development": ["Leadership Pipeline", "Capability Building", "Coaching Culture"],
    "Leadership Pipeline": ["Succession Planning"],
    "Succession Planning": ["Critical roles have ready successors"],
    "Capability Building": ["Skill Development"],
    "Skill Development": ["Leaders equipped for future needs"],
    "Coaching Culture": ["Leadership Maturity"],
    "Leadership Maturity": ["Leaders grow leaders"],
    "Talent Management": ["Talent Acquisition", "Talent Retention", "Talent Differentiation"],
    "Talent Acquisition": ["Strategic Hiring"],
    "Strategic Hiring": ["Right talent in key roles"],
    "Talent Retention": ["Engagement Drivers"],
    "Engagement Drivers": ["High performers choose to stay"],
    "Talent Differentiation": ["Performance Recognition"],
    "Performance Recognition": ["Meritocracy visibly practiced"],
    "Culture & Values": ["Culture Definition", "Culture Reinforcement", "Culture Measurement"],
    "Culture Definition": ["Shared Beliefs"],
    "Shared Beliefs": ["Values clearly articulated"],
    "Culture Reinforcement": ["Role Modeling"],
    "Role Modeling": ["Leaders live the values daily"],
    "Culture Measurement": ["Behavioral Indicators"],
    "Behavioral Indicators": ["Culture assessed objectively"],
    "Employee Experience": ["Trust & Safety", "Well-being Focus", "Communication Effectiveness"],
    "Trust & Safety": ["Psychological Safety"],
    "Psychological Safety": ["People speak up without fear"],
    "Well-being Focus": ["Work-Life Balance"],
    "Work-Life Balance": ["Sustainable performance enabled"],
    "Communication Effectiveness": ["Transparency"],
    "Transparency": ["Clarity reduces uncertainty"]
}

egg = ["200IQ", "GENIUS", "COOLEST PERSON IN THE COSMOS", "BEST SCIENTIST"]

HTML = """
<!DOCTYPE html><head><script src="https://d3js.org/d3.v6.min.js"></script>
<style>
body{background:#020617;margin:0;overflow:hidden;color:#f8fafc;font-family:sans-serif}
#search-wrapper{position:absolute;width:100%;text-align:center;z-index:100;top:50%;transform:translateY(-50%);transition:all .8s cubic-bezier(.19,1,.22,1)}
.ui-active{top:6%!important;transform:translateY(0) scale(.75)!important}
input{background:rgba(15,23,42,.9);border:2px solid #3b82f6;color:#fff;padding:16px;width:380px;text-align:center;font-size:1.3rem;outline:0;border-radius:50px;backdrop-filter:blur(10px)}
svg{width:100vw;height:100vh}
.node circle{stroke-width:1.5px;cursor:pointer}
.node text{font-size:10px;fill:#fff;text-anchor:middle;pointer-events:none}
.link{stroke:#1e293b;stroke-opacity:.4;stroke-width:1.2px}
.egg circle{fill:#eab308!important;stroke:#fde047!important;filter:drop-shadow(0 0 10px #eab308)}
.egg text{fill:#000!important;font-weight:900}
</style></head><body>
<div id="search-wrapper"><input type="text" id="search-input" placeholder="hit enter to search..." autocomplete="off"></div>
<svg id="canvas"></svg>
<script>
const db={{data|tojson}},eggNodes={{egg|tojson}},svg=d3.select("svg"),width=window.innerWidth,height=window.innerHeight;
let nodes=[],links=[];
const sim=d3.forceSimulation().force("link",d3.forceLink().id(d=>d.id).distance(180)).force("charge",d3.forceManyBody().strength(-1800)).force("center",d3.forceCenter(width/2,height/2+70)).force("collide",d3.forceCollide().radius(90));
function handleSearch(){
const val=document.getElementById('search-input').value.trim(),lower=val.toLowerCase(),wrap=document.getElementById('search-wrapper');
if(lower==="mihir"){wrap.classList.add('ui-active');updateGraph("MIHIR",!0)}
else{let key=Object.keys(db).find(k=>k.toLowerCase()===lower);if(key){wrap.classList.add('ui-active');updateGraph(key,!1)}}
}
document.getElementById('search-input').addEventListener('keypress',e=>{if(e.key==='Enter')handleSearch()});
function updateGraph(root,isEgg){
svg.selectAll("*").transition().duration(300).style("opacity",0).remove();
setTimeout(()=>{
const children=isEgg?eggNodes:db[root];
nodes=[{id:root,isCenter:!0,isEgg:isEgg}];
links=[];
children.forEach(c=>{nodes.push({id:c,isCenter:!1,isEgg:isEgg});links.push({source:root,target:c})});
render()},350)
}
function render(){
const link=svg.append("g").selectAll("line").data(links).join("line").attr("class","link"),
node=svg.append("g").selectAll("g").data(nodes).join("g").attr("class",d=>d.isEgg?"node egg":"node")
.on("dblclick",(e,d)=>{if(!d.isEgg&&db[d.id]){document.getElementById('search-input').value=d.id;handleSearch()}})
.call(d3.drag().on("start",(e,d)=>{if(!e.active)sim.alphaTarget(.3).restart();d.fx=d.x;d.fy=d.y}).on("drag",(e,d)=>{d.fx=e.x;d.fy=e.y}).on("end",(e,d)=>{if(!e.active)sim.alphaTarget(0);d.fx=null;d.fy=null}));
node.append("circle").attr("r",d=>d.isCenter?70:60).attr("fill",d=>d.isCenter?"#2563eb":"#0f172a").attr("stroke","#3b82f6");
node.append("text").selectAll("tspan").data(d=>d.id.split(" ")).join("tspan").attr("x",0).attr("dy",(d,i)=>i===0?0:12).text(d=>d);
sim.nodes(nodes);sim.force("link").links(links);sim.alpha(1).restart();
sim.on("tick",()=>{link.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y).attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);node.attr("transform",d=>`translate(${d.x},${d.y})`)})
}
</script></body></html>
"""
@app.route('/')
def home():
    return render_template_string(HTML, data=data, egg=egg)


if __name__ == "__main__":
    app.run(debug=False)