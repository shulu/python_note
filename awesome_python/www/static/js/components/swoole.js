var chars = [
        '0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z'
    ];
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
        target_id:   999,
        date: Date.now()
    };
    // 把 msg 对象作为JSON格式字符串发送
    exampleSocket.send(JSON.stringify(msg));

    // 清空文本输入元素，为接收下一条消息做好准备。
    document.getElementById("send_msg").value = "";
}