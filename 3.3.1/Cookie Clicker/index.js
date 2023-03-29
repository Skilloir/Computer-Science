var score = 0;
var cursors = 0;
var cursorPrice = 5;

function buyCursor() {
   if (score >= cursorPrice) {
      score = score - cursorPrice;
      cursors = cursors + 1;
      cursorPrice = Math.round(cursorPrice * 1.15);
      
      document.getElementById("score").innerHTML = score;
      document.getElementById("cursorPrice").innerHTML = currentCursorPrice;
      document.getElementById("cursors").innerHTML = cursors;
   }
}

function addtoscore(amount) {
   score = score + amount;
   document.getElementById("score").innerHTML = score;
}


