// JSON data
const data = [
  {
    title: "Karate",
    items: [
      {
        title: "Fundamentals",
        subitems: [
          "Stances (Kihon):  Basic stances like shiko dachi, zenkutsu dachi, kiba dachi, and heiko dachi.",
          "Blocks (Uke): Techniques for defending against strikes and kicks. Common blocks include gedan barai, jodan uke, chudan uke, and shuto uke.",
          "Strikes (Tsuki): Punches with different parts of the hand, including gyakuzuki, oi zuki, and mae geri.",
          "Kicks (Geri): Different kicks, such as mae geri, yoko geri, mawashi geri, and ushiro geri.",
          "Breathing (Kokyu): Proper breathing techniques for power and balance.",
        ],
      },
      {
        title: "Basic Techniques",
        subitems: [
          "Combinations: Putting together blocks, strikes, and kicks in sequence.",
          "Self-Defense: Simple self-defense techniques against common attacks.",
          "Kata: Prearranged forms that practice technique and movements.",
        ],
      },
      {
        title: "Advanced Techniques",
        subitems: [
          "Sparring (Kumite): Controlled combat with an opponent.",
          "Breaking (Kihon): Breaking boards, bricks, or other objects with strikes and kicks.",
          "Advanced Kata: More complex kata that require greater skill and coordination.",
        ],
      },
      {
        title: "Philosophy and Spirit",
        subitems: [
          "Bushido: The code of the warrior, emphasizing respect, discipline, and integrity.",
          "Focus and Concentration: Mental training for calmness and focus.",
          "Self-Improvement:  Striving for constant improvement in physical and mental skills.",
        ],
      },
      {
        title: "Training Regimen",
        subitems: [
          "Warm-up:  Stretching and light cardio to prepare the body.",
          "Kihon Practice:  Refining basic techniques.",
          "Kata Practice:  Improving form, timing, and power.",
          "Kumite Practice:  Sparring to develop fighting skills and reflexes.",
          "Cool-down: Stretching and breathing exercises to aid recovery.",
        ],
      },
      {
        title: "Styles of Karate",
        subitems: [
          "Shotokan: One of the most popular styles, known for its linear movements and strong stances.",
          "Goju-ryu: Emphasizes both hard and soft techniques, utilizing both striking and grappling.",
          "Wado-ryu:  Emphasizes circular movements and blending with the opponent's force.",
          "Shito-ryu: Combines elements of Shotokan and Goju-ryu.",
        ],
      },
      {
        title: "Safety and Etiquette",
        subitems: [
          "Respect:  Show respect for your instructors, fellow students, and the dojo.",
          "Proper Attire: Wear appropriate karate uniform (gi).",
          "Discipline:  Follow the rules and instructions of your instructor.",
          "Safety:  Train safely to avoid injuries.",
        ],
      },
      {
        title: "Benefits of Karate",
        subitems: [
          "Physical Fitness: Improves strength, flexibility, and cardiovascular health.",
          "Self-Defense Skills: Provides practical skills for personal safety.",
          "Mental Discipline:  Develops focus, concentration, and discipline.",
          "Confidence and Self-Esteem:  Boosts confidence and self-esteem through achievement.",
          "Stress Relief:  Provides a physical and mental outlet for stress.",
        ],
      },
    ],
  },
];

// Convert data to a hierarchical format
function renderTree() {
  const rootData = {
    name: data[0].title,
    children: data[0].items.map((item) => ({
      name: item.title,
      children: item.subitems.map((subitem) => ({ name: subitem })),
    })),
  };

  const width = window.innerWidth - 20;
  const height = window.innerHeight - 120;

  const svg = d3
    .select("#mynetwork")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .call(d3.zoom().on("zoom", zoomed))
    .append("g")
    .attr("transform", "translate(80,10)");

  // Current transform state
  let currentTransform = d3.zoomIdentity;

  // Handle zoom events for other interactions
  function zoomed(event) {
    currentTransform = event.transform;
    svg.attr("transform", currentTransform);
  }

  // Handle wheel events for panning
  d3.select("#mynetwork")
    .select("svg")
    .on("wheel", (event) => {
      event.preventDefault();
      const { deltaX, deltaY } = event;
      currentTransform = currentTransform.translate(-deltaX, -deltaY);
      svg.attr("transform", currentTransform);
    });

  const treeLayout = d3
    .tree()
    .size([height - height / 10, width - width / 3])
    .separation(
      (a, b) => (a.parent === b.parent ? 1 : 2) + (a.depth === 2 ? 0.5 : 0)
    ); // Adjust separation for leaf nodes

  const root = d3.hierarchy(rootData);

  treeLayout(root);

  const link = svg
    .selectAll(".link")
    .data(root.links())
    .enter()
    .append("path")
    .attr("class", "link")
    .attr(
      "d",
      d3
        .linkHorizontal()
        .x((d) => d.y)
        .y((d) => d.x)
    );

  const node = svg
    .selectAll(".node")
    .data(root.descendants())
    .enter()
    .append("g")
    .attr("class", "node")
    .attr("transform", (d) => `translate(${d.y},${d.x})`)
    .on("click", (event, d) => {
      navigator.clipboard.writeText(d.data.name)
    });

  node.append("circle").attr("r", 5);

  node
    .append("text")
    .attr("dy", 3)
    .attr("x", (d) => (d.children ? -8 : 8))
    .style("text-anchor", (d) => (d.children ? "end" : "start"))
    .text((d) => d.data.name);
}

// Initial render
renderTree();

document.getElementById("reloadBtn").addEventListener("click", () => {
  // Clear the existing SVG
  d3.select("#mynetwork").select("svg").remove();
  renderTree();
});