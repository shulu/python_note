const CLOSE_STATUS = {
    1000:{code:'CLOSE_NORMAL',des:"正常关闭"},
    1001:{code:'CLOSE_GOING_AWAY',des:"终端离开, 可能因为服务端错误, 也可能因为浏览器正从打开连接的页面跳转离开."},
    1002:{code:'CLOSE_PROTOCOL_ERROR',des:"由于协议错误而中断连接."},
    1003:{code:'CLOSE_UNSUPPORTED',des:"由于接收到不允许的数据类型而断开连接"},
    1005:{code:'CLOSE_NO_STATUS',des:"表示没有收到预期的状态码."},
    1006:{code:'CLOSE_ABNORMAL',des:"用于期望收到状态码时连接非正常关闭 "},
    1007:{code:'Unsupported Data',des:"由于收到了格式不符的数据而断开连接 "},
    1008:{code:'Policy Violation',des:"由于收到不符合约定的数据而断开连接"},
    1009:{code:'CLOSE_TOO_LARGE',des:"由于收到过大的数据帧而断开连接."},
    1010:{code:'Missing Extension',des:"客户端期望服务器商定一个或多个拓展, 但服务器没有处理, 因此客户端断开连接."},
    1011:{code:'Internal Error',des:"客户端由于遇到没有预料的情况阻止其完成请求, 因此服务端断开连接."},
    1012:{code:'Service Restart',des:"服务器由于重启而断开连接"},
    1013:{code:'Try Again Later',des:"服务器由于临时原因断开连接, 如服务器过载因此断开一部分客户端连接"},
    1015:{code:'TLS Handshake',des:"表示连接由于无法完成 TLS 握手而关闭"}

};
var chars = [
        '0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z'
    ];
var client_id = 0, server_id = 999, client_name = '';
var Socket ='';
initSocket();
Socket.onopen = function (event) {
    //exampleSocket.send(JSON.stringify());
    console.log('this is ok')
};
Socket.onmessage = function(event) {
    message = event.data;
    parse_message =  JSON.parse(message);
    client_id = parse_message.target_id;
    server_id = parse_message.from_id;
    recieve_message = parse_message.message;
    // console.log(parse_message);
    var f = document.getElementById("chat_box");
    // console.log(f)
    var text = "<p>";
    var time = new Date(parse_message.date);
    var timeStr = time.toLocaleTimeString("zh-CN");
    text += "<strong> "+server_id+": Send in "+timeStr+"</strong> <br>"+recieve_message;
    text += "</p>";
    if (text.length) {
        ele = $(text).get(0);
        f.appendChild(ele)
    }
};
Socket.onerror = function (event) {console.log(event)};
Socket.onclose = function (event) {console.log(event)};

function initSocket() {Socket = new WebSocket("ws:127.0.0.1:9501");}
function generateMixed(n) {
    var res = "";
    for(var i = 0; i < n ; i ++) {
        var id = Math.ceil(Math.random()*35);
        res += chars[id];
    }
    return res;
}
// 服务器向所有用户发送文本
function sendText() {
    // 构造一个 msg 对象， 包含了服务器处理所需的数据
    var msg = {
        type: "message",
        message: document.getElementById("send_msg").value,
        from_id:   client_id,
        target_id:   client_id,
        date: Date.now()
    };
    // 把 msg 对象作为JSON格式字符串发送
    Socket.send(JSON.stringify(msg));

    // 清空文本输入元素，为接收下一条消息做好准备。
    document.getElementById("send_msg").value = "";
}