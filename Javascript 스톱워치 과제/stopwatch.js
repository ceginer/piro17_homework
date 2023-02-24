let seconds = 0;
let tenMillis = 0;

const appendtenMillis = document.querySelector("#tenMillis");
const appendseconds = document.querySelector("#seconds");
const buttonStart = document.querySelector('#start');
const buttonStop = document.querySelector('#stop');
const buttonReset = document.querySelector('#reset');
let intervalId;
let click = 0;


// Start 버튼 함수
function opreateTimer() {
  tenMillis++;
  appendtenMillis.textContent = tenMillis > 9 ? tenMillis : '0' + tenMillis;
  if(tenMillis > 99) {
    seconds++;
    appendseconds.textContent = seconds > 9 ? seconds : '0' + seconds; 
    tenMillis = 0;
    appendtenMillis = "00"
  }
}

// start 버튼 , setInterval (함수, 밀리초) = 밀리초마다 함수 실행
// setInterval 은 0이 아닌 정수 ID 를 돌려준다
// clearinterval은 그것을 처음으로 만들어주는것
buttonStart.addEventListener('click',() => {
  clearInterval(intervalId)
  intervalId = setInterval(opreateTimer, 10)
})


// stop 버튼 + record 기능

// innerHTML 은 덮어씌어지기 때문에 div의 class 이름을 다르게 해서 각기 다르게 interHTML 이 적용되도록 했다.
buttonStop.addEventListener('click',() => {
  clearInterval(intervalId) ;

  click++;
  let nowTime = `${seconds > 9 ? seconds : '0' + seconds}:${tenMillis > 9 ? tenMillis : '0' + tenMillis}`;
  const newLog = document.querySelector('#logplus');
  const makeDiv = document.createElement('div');
  makeDiv.classList.add(`target${click}`);
  makeDiv.classList.add(`class-div`);
  newLog.appendChild(makeDiv);
  const aa= document.querySelector(`.target${click}`)
  aa.innerHTML=`<input type='checkbox' class='margin3'/><span class='now${click} class-h'></span><div class="class-mini"></div>`
  const targetDo = document.querySelector(`.now${click}`)
  targetDo.textContent = nowTime


})

// reset 버튼 + record 기록 삭제
buttonReset.addEventListener('click', () => {
  clearInterval(intervalId)
  tenMillis =0; 
  seconds = 0;
  appendseconds.textContent = '00';
  appendtenMillis.textContent = '00';

})

// 체크박스 모두 체크 or 모두 체크 해제
function selectAll(selectAll)  {
  const checkboxes 
    = document.querySelectorAll('input[type="checkbox"]');
  
  checkboxes.forEach((checkbox) => {
    checkbox.checked = selectAll.checked
  })
}

// 체크한거 삭제하는 함수

function del() {
  const checkboxes 
    = document.querySelectorAll('input[type="checkbox"]');
  
    for(let i = 1; i<checkboxes.length; i++){
      let box = checkboxes[i]
      if(box.checked){
        let delbox = box.parentNode
        delbox.parentNode.removeChild(delbox)
      }
    }
  const uncheck = document.querySelector('#log input')
  uncheck.checked = false
}
