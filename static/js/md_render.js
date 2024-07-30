document.addEventListener("DOMContentLoaded", function () {
    console.log("Topic:", topic);

    fetch(`/resources/${topic}_resource.md`)
        .then(response => response.text())
        .then(data => {
            console.log("Data:", data);
            document.getElementById('content').innerHTML = marked.parse(data);
        })
        .catch(error => console.error('Error fetching the markdown file:', error));
});



let fetched_news = false;
document.getElementById('load-news-button').addEventListener('click', function () {
    if (!fetched_news) {
        fetch(`/resources/${topic} Latest News.json`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const container = document.getElementById('yt-news-container');

                data.forEach(video => {
                    const videoDiv = document.createElement('div');
                    videoDiv.className = 'video';
                    videoDiv.style.display = "inline-block";
                    videoDiv.style.margin = "20px"

                    const iframe = document.createElement('iframe');
                    iframe.width = '560';
                    iframe.height = '315';
                    iframe.src = video.url;
                    iframe.title = "YouTube video player";
                    iframe.frameBorder = '0';
                    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
                    iframe.allowFullscreen = true;

                    videoDiv.appendChild(iframe);
                    container.appendChild(videoDiv);
                })
            });
        fetched_news = true;
    }

    if (document.getElementById('yt-news-container').style.visibility === 'hidden') {
        document.getElementById('yt-news-container').style.visibility = 'visible'
    }
    else if (document.getElementById('yt-news-container').style.visibility === 'visible') {
        document.getElementById('yt-news-container').style.visibility = 'hidden'
    }
});



let fetched_tutorial = false;
document.getElementById('load-tutorial-button').addEventListener('click', function () {
    if (!fetched_tutorial) {
        fetch(`/resources/${topic} Tutorial.json`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const container = document.getElementById('yt-tutorial-container');

                data.forEach(video => {
                    const videoDiv = document.createElement('div');
                    videoDiv.className = 'video';
                    videoDiv.style.display = "inline-block";
                    videoDiv.style.margin = "20px"

                    const iframe = document.createElement('iframe');
                    iframe.width = '560';
                    iframe.height = '315';
                    iframe.src = video.url;
                    iframe.title = "YouTube video player";
                    iframe.frameBorder = '0';
                    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
                    iframe.allowFullscreen = true;

                    videoDiv.appendChild(iframe);
                    container.appendChild(videoDiv);
                })
            });
        fetched_tutorial = true;
    }

    if (document.getElementById('yt-tutorial-container').style.visibility === 'hidden') {
        document.getElementById('yt-tutorial-container').style.visibility = 'visible'
    }
    else if (document.getElementById('yt-tutorial-container').style.visibility === 'visible') {
        document.getElementById('yt-tutorial-container').style.visibility = 'hidden'
    }
});


// document.addEventListener("DOMContentLoaded", function() {
//     const scrollContainer = document.getElementById('yt-news-container');
//     const scrollLeftButton = document.getElementById('scroll-left');
//     const scrollRightButton = document.getElementById('scroll-right');
//     const scrollAmount = 10; // Amount to scroll each step
//     let scrollInterval;

//     function startScrolling(direction) {
//         stopScrolling(); // Stop any existing scrolling
//         scrollInterval = setInterval(() => {
//             scrollContainer.scrollBy({
//                 left: direction * scrollAmount,
//                 behavior: 'smooth'
//             });
//         }, 150); // Repeat every 50ms
//     }

//     function stopScrolling() {
//         clearInterval(scrollInterval);
//     }

//     scrollLeftButton.addEventListener('mouseover', function() {
//         startScrolling(-1.5); // Scroll left
//     });

//     scrollRightButton.addEventListener('mouseover', function() {
//         startScrolling(1.5); // Scroll right
//     });

//     scrollLeftButton.addEventListener('mouseout', stopScrolling);
//     scrollRightButton.addEventListener('mouseout', stopScrolling);

//     // Optionally, you can add code to disable the buttons when the start/end is reached
//     scrollContainer.addEventListener('scroll', function() {
//         const maxScrollLeft = scrollContainer.scrollWidth - scrollContainer.clientWidth;
//         scrollLeftButton.disabled = scrollContainer.scrollLeft <= 0;
//         scrollRightButton.disabled = scrollContainer.scrollLeft >= maxScrollLeft;
//         scrollLeftButton.classList.toggle('hidden', scrollContainer.scrollLeft <= 0);
//         scrollRightButton.classList.toggle('hidden', scrollContainer.scrollLeft >= maxScrollLeft);
//     });

//     // Initial check to disable buttons if necessary
//     scrollContainer.dispatchEvent(new Event('scroll'));
// });

