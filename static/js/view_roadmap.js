fetch(`/roadmap/${topic}.json`)
    .then(response => response.json())
    .then(data => {
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
    })

    document.getElementById('resource').onclick = function () {
        window.open('/resources.html', '_blank');
    
    }