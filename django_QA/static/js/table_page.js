// 定义一个数组，保存当前所有页面的class name
var page_index = ["page-1", "page-2", "page-3"];

// 输入pagename，打开指定的div，隐藏其他的div
function page_option(pagename) {
    var tar_index = page_index.indexOf(pagename);
    page_index.slice(tar_index, 1);
    for (var j = 0; j < page_index.length; j++) {
        var close_div = document.getElementsByClassName(page_index[j]);
        for (var i = 0; i < close_div.length; i++) {
            close_div[i].style.display = "none";
        }
        ;
    }

    var opendiv = document.getElementsByClassName(pagename);
    for (var i = 0; i < opendiv.length; i++) {
        opendiv[i].style.display = "block";
    }
    ;
}

// 点击 返回第一页按钮 执行的操作
function first_click() {
    window.location.href='http://10.225.21.132:8888/QAPlatform/code_git/diff_check';
    window.alert("触发");

}

// 点击 跳到最后一页按钮 执行的操作
function last_click() {
    var total_page = document.getElementById('totalPage').value;
    page_option(page_index[page_index.length - 1]);
    document.getElementById('currentPage').value = total_page;
}

// 点击 上一页按钮 执行的操作
function prev_click() {
    var cur_page = document.getElementById('currentPage').value;
    if (cur_page > 1) {
        document.getElementById('currentPage').value = parseInt(cur_page) - 1;
        var pagename = page_index[parseInt(cur_page) - 2];
        page_option(pagename);
    }
}

// 点击 下一页按钮 执行的操作
function next_click() {
    var cur_page = document.getElementById('currentPage').value;
    var total_page = document.getElementById('totalPage').value;
    if (cur_page < total_page) {
        document.getElementById('currentPage').value = parseInt(cur_page) + 1;
        var pagename = page_index[parseInt(cur_page)];
        page_option(pagename);
    }
}

// 手动改变当前页码时执行的操作
function choose_page() {
    var cur_page = document.getElementById('currentPage').value;
    var pagename = page_index[parseInt(cur_page) - 1];
    page_option(pagename);
}

// 鼠标事件，经过每一条资讯时改变标题的颜色
function light(obj) {
    obj.firstElementChild.style.color = "#FF9900";
}

function normal(obj) {
    obj.firstElementChild.style.color = "#000000";
}
