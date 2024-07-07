fetch(`/roadmap/${topic}.json`)
    .then(response => response.json())
    .then(data => {
        const nodes = [];
        const edges = [];
        let nodeId = 1;

        function addNode(label, parentId = null, group = 'default') {
            const id = nodeId++;
            nodes.push({ id, label, group });
            if (parentId !== null) {
                edges.push({ from: parentId, to: id });
            }
            return id;
        }

        data.forEach(section => {
            const sectionId = addNode(section.title);
            section.items.forEach(item => {
                const itemId = addNode(item.title, sectionId, 'parent');
                item.subitems.forEach(subitem => {
                    addNode(subitem, itemId, 'leaf');
                });
            });
        });

        const container = document.getElementById('mynetwork');
        const networkData = {
            nodes: new vis.DataSet(nodes),
            edges: new vis.DataSet(edges)
        };
        const options = {
            layout: {
                hierarchical: {
                    enabled: true,
                    direction: 'LR', // Left to Right direction
                    sortMethod: 'directed', // Sort method for the tree layout
                    nodeSpacing: 200, // Adjusted node spacing
                    levelSeparation: 300, // Adjusted level separation
                }
            },
            interaction: {
                dragView: true, // Enable dragging/panning
                zoomView: false // Disable zoom on scroll
            },
            physics: false // Disable physics to prevent automatic repositioning
        };
        const network = new vis.Network(container, networkData, options);

        container.addEventListener('wheel', function (event) {
            event.preventDefault();
            const direction = event.deltaY > 0 ? -0.4 : 0.4;
            const viewPosition = network.getViewPosition();
            const moveAmount = 50; // Amount of pixels to move

            network.moveTo({
                position: { x: viewPosition.x, y: viewPosition.y - direction * moveAmount },
                offset: { x: 0, y: 0 },
                animation: true
            });
        });

        document.getElementById('zoomIn').onclick = function () {
            const scale = network.getScale();
            network.moveTo({
                scale: scale * 1.2
            });
        };

        document.getElementById('zoomOut').onclick = function () {
            const scale = network.getScale();
            network.moveTo({
                scale: scale / 1.2
            });
        };

        // Add event listener for node click
        network.on('click', function (params) {
            var node = network.getNodeAt(params.pointer.DOM);
            if (node !== undefined) {
                var nodeName = nodes[node - 1].label;
                copyToClipboard(nodeName);
            }
        });

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function () {
            }, function (err) {
                console.error('Could not copy text: ', err);
            });
        }

        let scale_ = network.getScale();
        network.moveTo({
            scale: scale_*10 
        })
    })
    .catch(error => console.error('Error fetching roadmap JSON:', error));


document.getElementById('resources').onclick = function () {
    window.open('/resources.html', '_blank');

}

