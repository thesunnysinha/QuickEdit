const sidebar = document.getElementById("sidebar-wrapper");
const header = document.getElementById("header");
const content = document.getElementById("content");
const footer = document.getElementById("footer");
const hammer = document.getElementById("hammer");

hammer.addEventListener("click", () => {
  sidebar.classList.toggle("open");

  if (sidebar.classList.contains("open")) {
    header.style.marginLeft = "250px"; 
    content.style.marginLeft = "250px"; 
    footer.style.marginLeft = "250px";
  } else {
    header.style.marginLeft = "0";
    content.style.marginLeft = "0";
    footer.style.marginLeft = "0";
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var searchInput = document.getElementById("searchInput");
  var sidebarList = document.getElementById("sidebarList");

  searchInput.addEventListener("keyup", function () {
    var searchText = searchInput.value.toLowerCase();
    var listItems = sidebarList.getElementsByTagName("li");

    for (var i = 0; i < listItems.length; i++) {
      var listItem = listItems[i];
      var itemText = listItem.textContent || listItem.innerText;
      itemText = itemText.toLowerCase();

      if (itemText.indexOf(searchText) !== -1) {
        listItem.style.display = "block";
      } else {
        listItem.style.display = "none";
      }
    }
  });
});


// JavaScript code for real-time search and filtering (same as previous examples)
document.addEventListener("DOMContentLoaded", function() {
    var fullscreenBtn = document.getElementById("fullscreen-btn");

    fullscreenBtn.addEventListener("click", function() {
        toggleFullScreen();
    });
});

function toggleFullScreen() {
    var doc = window.document;
    var docEl = doc.documentElement;

    var requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
    var exitFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;

    if (!doc.fullscreenElement && !doc.mozFullScreenElement && !doc.webkitFullscreenElement && !doc.msFullscreenElement) {
        // If the document is not in fullscreen mode, request it.
        if (requestFullScreen) {
            requestFullScreen.call(docEl);
        }
    } else {
        // Otherwise, exit fullscreen mode.
        if (exitFullScreen) {
            exitFullScreen.call(doc);
        }
    }
}

