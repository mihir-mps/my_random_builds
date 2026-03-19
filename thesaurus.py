from flask import Flask, render_template_string

app = Flask(__name__)

application = app

data = {
    "CEO": ["STRATEGIC MANAGEMENT", "SYSTEM MANAGEMENT", "PEOPLE MANAGEMENT"],
    "STRATEGIC MANAGEMENT": ["VISION & DIRECTION", "STRATEGIC THINKING", "GROWTH STRATEGY", "GOVERNANCE & STEWARDSHIP"],
    "VISION & DIRECTION": ["VISION FORMULATION", "VISION COMMUNICATION"],
    "VISION FORMULATION": ["LONG-TERM ASPIRATION", "STRATEGIC NARRATIVE"],
    "LONG-TERM ASPIRATION": ["CLEAR COMPELLING FUTURE STATE ARTICULATED"],
    "STRATEGIC NARRATIVE": ["VISION TRANSLATED INTO UNDERSTANDABLE STORY"],
    "VISION COMMUNICATION": ["LEADERSHIP ALIGNMENT", "ORGANIZATION BUY-IN"],
    "LEADERSHIP ALIGNMENT": ["TOP TEAM CONSISTENTLY REINFORCES VISION"],
    "ORGANIZATION BUY-IN": ["EMPLOYEES UNDERSTAND STRATEGIC INTENT"],
    "STRATEGIC THINKING": ["ENVIRONMENTAL SCANNING", "STRATEGIC CHOICE"],
    "ENVIRONMENTAL SCANNING": ["MARKET INTELLIGENCE", "COMPETITIVE ANALYSIS"],
    "MARKET INTELLIGENCE": ["CONTINUOUS MONITORING OF MARKET FORCES"],
    "COMPETITIVE ANALYSIS": ["CLEAR UNDERSTANDING OF COMPETITORS MOVES"],
    "STRATEGIC CHOICE": ["TRADE-OFF DECISIONS", "RESOURCE PRIORITIZATION"],
    "TRADE-OFF DECISIONS": ["CONSCIOUS SELECTION OF WHAT NOT TO PURSUE"],
    "RESOURCE PRIORITIZATION": ["CAPITAL ALIGNED TO STRATEGIC PRIORITIES"],
    "GROWTH STRATEGY": ["OPPORTUNITY IDENTIFICATION", "STRATEGIC INVESTMENT"],
    "OPPORTUNITY IDENTIFICATION": ["NEW MARKET EXPLORATION", "PRODUCT OR SERVICE EXPANSION"],
    "NEW MARKET EXPLORATION": ["VIABLE GROWTH AVENUES IDENTIFIED"],
    "PRODUCT OR SERVICE EXPANSION": ["PORTFOLIO ALIGNED TO DEMAND TRENDS"],
    "STRATEGIC INVESTMENT": ["INORGANIC GROWTH", "ORGANIC SCALING"],
    "INORGANIC GROWTH": ["MERGERS OR PARTNERSHIPS EVALUATED PRUDENTLY"],
    "ORGANIC SCALING": ["CORE BUSINESS SCALED SUSTAINABLY"],
    "GOVERNANCE & STEWARDSHIP": ["BOARD ENGAGEMENT", "RISK OVERSIGHT", "ETHICAL LEADERSHIP"],
    "BOARD ENGAGEMENT": ["GOVERNANCE EFFECTIVENESS"],
    "GOVERNANCE EFFECTIVENIVENESS": ["BOARD DECISIONS ADD STRATEGIC VALUE"],
    "RISK OVERSIGHT": ["ENTERPRISE RISK VIEW"],
    "ENTERPRISE RISK VIEW": ["KEY RISKS ANTICIPATED AND MITIGATED"],
    "ETHICAL LEADERSHIP": ["VALUES-BASED DECISIONS"],
    "VALUES-BASED DECISIONS": ["TRUST AND INTEGRITY INSTITUTIONALIZED"],
    "SYSTEM MANAGEMENT": ["ORGANIZATIONAL DESIGN", "PROCESS EXCELLENCE", "TECHNOLOGY & DIGITAL", "PERFORMANCE MANAGEMENT"],
    "ORGANIZATIONAL DESIGN": ["STRUCTURE DESIGN", "OPERATING MODEL"],
    "STRUCTURE DESIGN": ["ROLE CLARITY", "DECISION RIGHTS"],
    "ROLE CLARITY": ["CLEAR ACCOUNTABILITY ACROSS FUNCTIONS"],
    "DECISION RIGHTS": ["DECISIONS MADE AT THE RIGHT LEVEL"],
    "OPERATING MODEL": ["END-TO-END FLOW"],
    "END-TO-END FLOW": ["WORK MOVES SEAMLESSLY ACROSS UNITS"],
    "PROCESS EXCELLENCE": ["PROCESS STANDARDIZATION", "PROCESS OPTIMIZATION", "CONTINUOUS IMPROVEMENT"],
    "PROCESS STANDARDIZATION": ["SOP DEFINITION"],
    "SOP DEFINITION": ["CONSISTENT EXECUTION ACROSS ORGANIZATION"],
    "PROCESS OPTIMIZATION": ["WASTE ELIMINATION"],
    "WASTE ELIMINATION": ["REDUCED INEFFICIENCIES AND REWORK"],
    "CONTINUOUS IMPROVEMENT": ["FEEDBACK LOOPS"],
    "FEEDBACK LOOPS": ["PROCESSES REFINED USING DATA"],
    "TECHNOLOGY & DIGITAL": ["DIGITAL STRATEGY", "SYSTEM INTEGRATION", "AUTOMATION ENABLEMENT"],
    "DIGITAL STRATEGY": ["TECHNOLOGY ROADMAP"],
    "TECHNOLOGY ROADMAP": ["IT ALIGNED WITH BUSINESS STRATEGY"],
    "SYSTEM INTEGRATION": ["DATA FLOW INTEGRITY"],
    "DATA FLOW INTEGRITY": ["SINGLE SOURCE OF TRUTH ESTABLISHED"],
    "AUTOMATION ENABLEMENT": ["PRODUCTIVITY GAINS"],
    "PRODUCTIVITY GAINS": ["MANUAL EFFORT SYSTEMATICALLY REDUCED"],
    "PERFORMANCE MANAGEMENT": ["KPI FRAMEWORK", "MONITORING & REVIEW", "CORRECTIVE ACTION"],
    "KPI FRAMEWORK": ["METRIC DEFINITION"],
    "METRIC DEFINITION": ["MEASURES REFLECT STRATEGIC PRIORITIES"],
    "MONITORING & REVIEW": ["PERFORMANCE CADENCE"],
    "PERFORMANCE CADENCE": ["REGULAR DISCIPLINED REVIEWS CONDUCTED"],
    "CORRECTIVE ACTION": ["COURSE CORRECTION"],
    "COURSE CORRECTION": ["TIMELY INTERVENTIONS IMPROVE OUTCOMES"],
    "PEOPLE MANAGEMENT": ["LEADERSHIP DEVELOPMENT", "TALENT MANAGEMENT", "CULTURE & VALUES", "EMPLOYEE EXPERIENCE"],
    "LEADERSHIP DEVELOPMENT": ["LEADERSHIP PIPELINE", "CAPABILITY BUILDING", "COACHING CULTURE"],
    "LEADERSHIP PIPELINE": ["SUCCESSION PLANNING"],
    "SUCCESSION PLANNING": ["CRITICAL ROLES HAVE READY SUCCESSORS"],
    "CAPABILITY BUILDING": ["SKILL DEVELOPMENT"],
    "SKILL DEVELOPMENT": ["LEADERS EQUIPPED FOR FUTURE NEEDS"],
    "COACHING CULTURE": ["LEADERSHIP MATURITY"],
    "LEADERSHIP MATURITY": ["LEADERS GROW LEADERS"],
    "TALENT MANAGEMENT": ["TALENT ACQUISITION", "TALENT RETENTION", "TALENT DIFFERENTIATION"],
    "TALENT ACQUISITION": ["STRATEGIC HIRING"],
    "STRATEGIC HIRING": ["RIGHT TALENT IN KEY ROLES"],
    "TALENT RETENTION": ["ENGAGEMENT DRIVERS"],
    "ENGAGEMENT DRIVERS": ["HIGH PERFORMERS CHOOSE TO STAY"],
    "TALENT DIFFERENTIATION": ["PERFORMANCE RECOGNITION"],
    "PERFORMANCE RECOGNITION": ["MERITOCRACY VISIBLY PRACTICED"],
    "CULTURE & VALUES": ["CULTURE DEFINITION", "CULTURE REINFORCEMENT", "CULTURE MEASUREMENT"],
    "CULTURE DEFINITION": ["SHARED BELIEFS"],
    "SHARED BELIEFS": ["VALUES CLEARLY ARTICULATED"],
    "CULTURE REINFORCEMENT": ["ROLE MODELING"],
    "ROLE MODELING": ["LEADERS LIVE THE VALUES DAILY"],
    "CULTURE MEASUREMENT": ["BEHAVIORAL INDICATORS"],
    "BEHAVIORAL INDICATORS": ["CULTURE ASSESSED OBJECTIVELY"],
    "EMPLOYEE EXPERIENCE": ["TRUST & SAFETY", "WELL-BEING FOCUS", "COMMUNICATION EFFECTIVENESS"],
    "TRUST & SAFETY": ["PSYCHOLOGICAL SAFETY"],
    "PSYCHOLOGICAL SAFETY": ["PEOPLE SPEAK UP WITHOUT FEAR"],
    "WELL-BEING FOCUS": ["WORK-LIFE BALANCE"],
    "WORK-LIFE BALANCE": ["SUSTAINABLE PERFORMANCE ENABLED"],
    "COMMUNICATION EFFECTIVENESS": ["TRANSPARENCY"],
    "TRANSPARENCY": ["CLARITY REDUCES UNCERTAINTY"]
}

egg = ["200IQ", "GENIUS", "COOLEST PERSON IN THE COSMOS", "BEST SCIENTIST", "THEORETICAL PHYSICIST"]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style>
        body { background: #020617; margin: 0; overflow: hidden; color: #f8fafc; font-family: sans-serif; }
        
        #tree-panel {
            width: 0; position: fixed; left: 0; top: 0; height: 100vh;
            transition: width 0.4s ease; overflow-y: auto; overflow-x: hidden;
            background: rgba(15, 23, 42, 0.98); border-right: 1px solid #3b82f6; z-index: 1500;
        }
        .tree-item { 
            cursor: pointer; display: block; padding: 6px 15px; 
            font-size: 10px; color: #94a3b8; text-transform: uppercase;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
            max-width: 380px;
        }
        .tree-item:hover { color: #3b82f6; background: rgba(59, 130, 246, 0.1); }

        #header-area {
            position: fixed; top: 30px; width: 100%; text-align: center; z-index: 100; pointer-events: none;
        }
        #main-heading {
            color: #3b82f6; font-size: 1.5rem; font-weight: 800; letter-spacing: 4px;
            margin: 0; text-transform: uppercase;
        }

        #search-container {
            position: absolute; width: 100%; text-align: center; z-index: 101;
            top: 50%; transform: translateY(-50%);
            transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }
        #search-container.active { top: 85px; transform: translateY(0); }

        input {
            background: rgba(15, 23, 42, .95); border: 2px solid #3b82f6; color: #fff;
            padding: 15px 30px; width: 400px; text-align: center; border-radius: 50px; 
            outline: 0; font-size: 1rem; transition: all 0.4s ease;
            pointer-events: auto;
        }
        #search-container.active input { padding: 8px 20px; width: 300px; font-size: 0.85rem; }

        #note-panel {
            position: fixed; display: none; background: #1e293b; border: 1px solid #3b82f6;
            border-radius: 8px; padding: 12px; z-index: 3000; width: 220px;
        }
        textarea { width: 100%; height: 80px; background: #020617; color: white; border: 1px solid #334155; padding: 5px; font-size: 11px; resize: none; }

        .node circle { cursor: pointer; }
        .node text { font-size: 9px; fill: #fff; text-anchor: middle; pointer-events: none; font-weight: bold; text-transform: uppercase; }
        .link { stroke: #334155; stroke-opacity: 0.4; stroke-width: 2px; }
        .menu-dots { cursor: pointer; opacity: 0.6; }
        
        #canvas { opacity: 0; transition: opacity 1s ease; }
        #canvas.visible { opacity: 1; }

        /* Mihir Overlay Style */
        #mihir-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95); z-index: 9999; display: none;
            flex-direction: column; justify-content: center; align-items: center;
            color: #3b82f6; font-family: 'Courier New', Courier, monospace;
            text-shadow: 0 0 10px #3b82f6;
        }
    </style>
</head>
<body>
    <button id="btn-tree" style="position:absolute; top:20px; left:20px; z-index:2000; background:#3b82f6; color:white; border:none; padding:8px 15px; cursor:pointer; border-radius:4px; font-weight:bold;">☰ STRUCTURE</button>
    
    <div id="tree-panel"><div id="tree-content" style="padding: 80px 10px 40px 10px;"></div></div>

    <div id="header-area">
        <div id="main-heading">Strategy Map</div>
    </div>

    <div id="search-container">
        <input type="text" id="search-input" placeholder="hit enter to search..." autocomplete="off">
    </div>

    <div id="note-panel">
        <div id="note-title" style="font-size:10px; color:#3b82f6; margin-bottom:5px; font-weight:bold;"></div>
        <textarea id="note-text"></textarea>
        <button onclick="saveNote()" style="width:100%; margin-top:8px; background:#3b82f6; color:white; border:none; padding:6px; cursor:pointer; font-size:10px; font-weight:bold;">SAVE</button>
    </div>

    <div id="mihir-overlay">
        <h1 style="letter-spacing: 15px; border-bottom: 2px solid #3b82f6; padding-bottom: 10px;">MIHIR: IDENTITY VERIFIED</h1>
        <div id="egg-content" style="margin-top: 20px; font-size: 1.2rem; line-height: 2;"></div>
        <button onclick="document.getElementById('mihir-overlay').style.display='none'" style="margin-top: 40px; background: transparent; color: #3b82f6; border: 1px solid #3b82f6; padding: 10px 20px; cursor: pointer;">CLOSE SYSTEM ACCESS</button>
    </div>

    <svg id="canvas"></svg>

    <script>
        const db = {{ data|tojson }};
        const eggs = {{ egg|tojson }};
        const svg = d3.select("#canvas").attr("width", window.innerWidth).attr("height", window.innerHeight);
        const searchBox = document.getElementById('search-container');
        const searchInput = document.getElementById('search-input');
        
        let nodes = [], links = [], activeNoteId = null;

        const sim = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id).distance(180))
            .force("charge", d3.forceManyBody().strength(-2000))
            .force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2 + 60))
            .force("collide", d3.forceCollide().radius(90));

        function makeTree(node, depth=0) {
            let html = `<div style="margin-left:${depth*12}px; border-left: 1px solid rgba(59, 130, 246, 0.2);">
                        <span class="tree-item" title="${node}" onclick="jumpTo('${node}')">${node}</span>`;
            if(db[node]) db[node].forEach(c => html += makeTree(c, depth+1));
            return html + `</div>`;
        }
        document.getElementById('tree-content').innerHTML = makeTree("CEO");

        document.getElementById('btn-tree').onclick = () => {
            const p = document.getElementById('tree-panel');
            p.style.width = p.style.width === "400px" ? "0" : "400px";
        };

        function showMihir() {
            const overlay = document.getElementById('mihir-overlay');
            const content = document.getElementById('egg-content');
            content.innerHTML = eggs.map(e => `<div>> ${e}</div>`).join("");
            overlay.style.display = 'flex';
            searchInput.value = "";
        }

        searchInput.addEventListener('keypress', e => { 
            if(e.key === 'Enter') {
                const val = searchInput.value.trim().toUpperCase();
                
                if (val === "MIHIR") {
                    showMihir();
                    return;
                }

                const keyExists = db[val] || Object.values(db).some(arr => arr.includes(val));
                if (keyExists) {
                    searchBox.classList.add('active');
                    document.getElementById('canvas').classList.add('visible');
                    updateGraph(val);
                }
            }
        });

        function jumpTo(id) { 
            searchInput.value = id; 
            searchBox.classList.add('active');
            document.getElementById('canvas').classList.add('visible');
            updateGraph(id.toUpperCase()); 
        }

        function updateGraph(root) {
            svg.selectAll("*").remove(); 
            let parentId = Object.keys(db).find(key => db[key].includes(root));
            const children = db[root] || [];
            nodes = []; links = [];

            if (parentId) { nodes.push({ id: parentId, isRoot: true }); links.push({ source: root, target: parentId }); }
            nodes.push({ id: root, isCenter: true });
            children.forEach(c => { nodes.push({ id: c }); links.push({ source: root, target: c }); });
            
            render();
        }

        function openNote(e, id) {
            e.stopPropagation(); activeNoteId = id;
            const panel = document.getElementById('note-panel');
            document.getElementById('note-title').innerText = "NODE: " + id;
            document.getElementById('note-text').value = localStorage.getItem('note_'+id) || "";
            panel.style.display = 'block';
            panel.style.left = Math.min(e.pageX, window.innerWidth - 240) + 'px'; 
            panel.style.top = Math.min(e.pageY, window.innerHeight - 150) + 'px';
        }
        
        function saveNote() { 
            localStorage.setItem('note_'+activeNoteId, document.getElementById('note-text').value); 
            document.getElementById('note-panel').style.display = 'none'; 
        }

        function render() {
            const linkGroup = svg.append("g").selectAll("line").data(links).join("line").attr("class", "link");
            const nodeGroup = svg.append("g").selectAll("g").data(nodes).join("g")
                .attr("class", "node")
                .on("dblclick", (e, d) => { if (!d.isCenter) jumpTo(d.id); })
                .call(d3.drag()
                    .on("start", (e,d) => { if(!e.active) sim.alphaTarget(0.3).restart(); d.fx=d.x; d.fy=d.y; })
                    .on("drag", (e,d) => { d.fx=e.x; d.fy=e.y; })
                    .on("end", (e,d) => { if(!e.active) sim.alphaTarget(0); d.fx=null; d.fy=null; }));

            nodeGroup.append("circle")
                .attr("r", d => d.isRoot ? 40 : (d.isCenter ? 65 : 50))
                .attr("fill", d => d.isRoot ? "#991b1b" : (d.isCenter ? "#2563eb" : "#0f172a"))
                .attr("stroke", d => d.isRoot ? "none" : "#3b82f6")
                .attr("stroke-width", d => d.isRoot ? 0 : 2);

            nodeGroup.append("text").selectAll("tspan").data(d => d.id.split(" ")).join("tspan")
                .attr("x", 0).attr("dy", (d,i) => i===0 ? 0 : 11).text(d => d);

            const dots = nodeGroup.append("g").attr("class", "menu-dots").on("click", (e,d) => openNote(e, d.id));
            [-6, 0, 6].forEach(cx => { dots.append("circle").attr("cx", cx).attr("cy", 32).attr("r", 2.5).attr("fill", "#64748b"); });

            sim.nodes(nodes); sim.force("link").links(links); sim.alpha(1).restart();
            sim.on("tick", () => {
                linkGroup.attr("x1", d=>d.source.x).attr("y1", d=>d.source.y).attr("x2", d=>d.target.x).attr("y2", d=>d.target.y);
                nodeGroup.attr("transform", d => `translate(${d.x},${d.y})`);
            });
        }

        window.addEventListener('resize', () => {
            svg.attr("width", window.innerWidth).attr("height", window.innerHeight);
            sim.force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2 + 60));
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, data=data, egg=egg)

if __name__ == "__main__":
    app.run(debug=False, port=8000)