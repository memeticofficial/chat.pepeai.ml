// Get a reference to the div you want to auto-scroll.
var someElement = document.querySelector('.dialogue');
console.log({someElement});
// Create an observer and pass it a callback.
var observer = new MutationObserver(scrollToBottom);
// Tell it to look for new children that will change the height.
var config = {childList: true};
observer.observe(someElement, config);

function scrollToBottom() {
console.log('scrolling');
console.log(someElement.scrollHeight);
  someElement.scrollTop = someElement.scrollHeight - someElement.clientHeight;
}
