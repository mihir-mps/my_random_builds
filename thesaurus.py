from flask import Flask, render_template_string

app = Flask(__name__)

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
    "GOVERNANCE EFFECTIVENESS": ["BOARD DECISIONS ADD STRATEGIC VALUE"],
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

egg = ["200IQ", "GENIUS", "COOLEST PERSON IN THE COSMOS", "BEST SCIENTIST"]


HTML = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style>
        body {
            background: #020617;
            margin: 0;
            overflow: hidden;
            color: #f8fafc;
            font-family: sans-serif;
        }

        #search-wrapper {
            position: absolute;
            width: 100%;
            text-align: center;
            z-index: 100;
            top: 50%;
            transform: translateY(-50%);
            transition: all 0.8s cubic-bezier(.19,1,.22,1);
        }

        .ui-active {
            top: 6% !important;
            transform: translateY(0) scale(.75) !important;
        }

        input {
            background: rgba(15, 23, 42, .9);
            border: 2px solid #3b82f6;
            color: #fff;
            padding: 16px;
            width: 380px;
            text-align: center;
            font-size: 1.3rem;
            outline: 0;
            border-radius: 50px;
            backdrop-filter: blur(10px);
        }

        svg {
            width: 100vw;
            height: 100vh;
        }

        .node circle {
            stroke-width: 1.5px;
            cursor: pointer;
        }

        .node text {
            font-size: 10px;
            fill: #fff;
            text-anchor: middle;
            pointer-events: none;
        }

        .link {
            stroke: #1e293b;
            stroke-opacity: .4;
            stroke-width: 1.2px;
        }

        .egg circle {
            fill: #eab308 !important;
            stroke: #fde047 !important;
        }

        .egg text {
            fill: #000 !important;
            font-weight: 900;
        }

        .root-node circle {
            fill: #7f1d1d !important;
            stroke: #991b1b !important;
        }
    </style>
</head>
<body>

    <div id="search-wrapper">
        <input type="text" id="search-input" placeholder="hit enter to search..." autocomplete="off">
    </div>

    <svg id="canvas"></svg>

    <script>
        const db = {{ data|tojson }};
        const eggNodes = {{ egg|tojson }};
        const svg = d3.select("svg");
        const width = window.innerWidth;
        const height = window.innerHeight;

        let nodes = [];
        let links = [];

        const sim = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id).distance(180))
            .force("charge", d3.forceManyBody().strength(-1800))
            .force("center", d3.forceCenter(width / 2, height / 2 + 70))
            .force("collide", d3.forceCollide().radius(90));

        function handleSearch() {
            const val = document.getElementById('search-input').value.trim();
            const lower = val.toLowerCase();
            const wrap = document.getElementById('search-wrapper');

            if (lower === "mihir") {
                wrap.classList.add('ui-active');
                updateGraph("MIHIR", true, null);
            } else {
                let key = Object.keys(db).find(k => k.toLowerCase() === lower);
                if (key) {
                    wrap.classList.add('ui-active');
                    updateGraph(key, false, null);
                }
            }
        }

        document.getElementById('search-input').addEventListener('keypress', e => {
            if (e.key === 'Enter') handleSearch();
        });

        function updateGraph(root, isEgg, parentId) {
            svg.selectAll("*")
               .transition()
               .duration(300)
               .style("opacity", 0)
               .remove();

            setTimeout(() => {
                const children = isEgg ? eggNodes : (db[root] || []);
                nodes = [];
                links = [];

                if (parentId) {
                    nodes.push({ id: parentId, isCenter: false, isEgg: false, isRoot: true });
                    links.push({ source: root, target: parentId });
                }

                nodes.push({ id: root, isCenter: true, isEgg: isEgg, isRoot: false });

                children.forEach(c => {
                    if (c !== parentId) {
                        nodes.push({ id: c, isCenter: false, isEgg: isEgg, isRoot: false });
                        links.push({ source: root, target: c });
                    }
                });

                render();
            }, 350);
        }

        function render() {
            const link = svg.append("g")
                .selectAll("line")
                .data(links)
                .join("line")
                .attr("class", "link");

            const node = svg.append("g")
                .selectAll("g")
                .data(nodes)
                .join("g")
                .attr("class", d => d.isRoot ? "node root-node" : (d.isEgg ? "node egg" : "node"))
                .on("dblclick", (e, d) => {
                    if (d.isRoot) {
                        let grandParent = Object.keys(db).find(key => db[key].includes(d.id));
                        document.getElementById('search-input').value = d.id;
                        updateGraph(d.id, false, grandParent || null);
                    } 
                    else if (!d.isEgg && db[d.id]) {
                        const currentCenter = nodes.find(n => n.isCenter).id;
                        document.getElementById('search-input').value = d.id;
                        updateGraph(d.id, false, currentCenter);
                    }
                })
                .call(d3.drag()
                    .on("start", (e, d) => {
                        if (!e.active) sim.alphaTarget(.3).restart();
                        d.fx = d.x;
                        d.fy = d.y;
                    })
                    .on("drag", (e, d) => {
                        d.fx = e.x;
                        d.fy = e.y;
                    })
                    .on("end", (e, d) => {
                        if (!e.active) sim.alphaTarget(0);
                        d.fx = null;
                        d.fy = null;
                    })
                );

            node.append("circle")
                .attr("r", d => d.isRoot ? 40 : (d.isCenter ? 70 : 60))
                .attr("fill", d => {
                    if (d.isRoot) return "#7f1d1d";
                    return d.isCenter ? "#2563eb" : "#0f172a";
                })
                .attr("stroke", d => d.isRoot ? "#991b1b" : "#3b82f6");

            node.append("text")
                .selectAll("tspan")
                .data(d => d.id.split(" "))
                .join("tspan")
                .attr("x", 0)
                .attr("dy", (d, i) => i === 0 ? 0 : 12)
                .text(d => d);

            sim.nodes(nodes);
            sim.force("link").links(links);
            sim.alpha(1).restart();

            sim.on("tick", () => {
                link.attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);
                
                node.attr("transform", d => `translate(${d.x},${d.y})`);
            });
        }
    </script>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(HTML, data=data, egg=egg)


if __name__ == "__main__":
    app.run(debug=False)