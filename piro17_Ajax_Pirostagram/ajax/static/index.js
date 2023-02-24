
const requestdel = new XMLHttpRequest();

const onClickDel = (id) => {
  const url = "/delete/";
  requestdel.open("POST", url, true);
  requestdel.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestdel.send(JSON.stringify({ id: id }));
};

requestdel.onreadystatechange = () => {
  if (requestdel.readyState === XMLHttpRequest.DONE) {
    if (requestdel.status < 400) {
      const { id } = JSON.parse(requestdel.response);
      const comment = document.querySelector(`#comment-${id}`);
      comment.remove();
    }
  }
};


const requestLike = new XMLHttpRequest();
const onClickLike = (id) => {
  const url = "/like/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(JSON.stringify({ id: id }));
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    const { id, type } = JSON.parse(requestLike.response); 
    // const element = document.querySelector(`#post-${id} .contentbox`);
    const i = document.querySelector(`#comment-${id} button i`);
    i.classList.toggle("far");
    i.classList.toggle("fas");
  }
};



const request = new XMLHttpRequest(); //ajax의 시작
const make_comment = (post_id) => {
  var inputValue = document.getElementById('comment').value;
  const url = "comment/";
  request.open("POST",url,true);
  request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
  request.send(JSON.stringify({ post_id : post_id, inputValue : inputValue })); // json 형태로 url로 보냈따
}

request.onreadystatechange = () =>{
  if (request.readyState == XMLHttpRequest.DONE) {
    if (request.status <= 400) {
    const {post_id, inputValue} = JSON.parse(request.response);
    const element = document.querySelector('#post-id-{{post.id}} #comment-{{comment.id}}')
    comment=Comment()
    comment.save()
    }
  }
};
