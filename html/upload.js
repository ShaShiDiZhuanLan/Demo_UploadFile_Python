/***********************************
Author: 沙振宇
CreateTime: 2019-7-29
UpdateTime: 2019-12-17
Info: 上传Excel文件
***********************************/
// 文件选择
function fileSelected() {
    var file = document.getElementById('fileToUpload').files[0];
    if (file) {
        var fileSize = 0;
        if (file.size > 1024 * 1024)
            fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
        else
            fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';
        document.getElementById('fileName').innerHTML = '<blockquote>文件名称: ' + file.name+'</blockquote>';
        document.getElementById('fileSize').innerHTML = '<blockquote>文件尺寸: ' + fileSize+'</blockquote>';
        document.getElementById('fileType').innerHTML = '<blockquote>文件类型: ' + file.type+'</blockquote>';
        document.getElementById('uploadFile').innerHTML = '<blockquote><input class="file_upload" type="button" onclick="onUploadFile()" value="上传"></blockquote>';
    }
}
//上传文件
function onUploadFile() {
    if (document.getElementById('fileToUpload').files.length === 0) {
        console.log("未选择文件");
        return;
    }
    var formData = new FormData();
    formData.append("exceldata", document.getElementById('fileToUpload').files[0]);
    console.log(formData);
    $.ajax({
        url:'http://127.0.0.1:9088/upload',
        type:'POST',
        data:formData,
        processData:false,  //tell jQuery not to process the data
        contentType: false,  //tell jQuery not to set contentType
        success:function (arg,a1,a2) {//这儿的三个参数其实就是XMLHttpRequest里面带的信息。
            console.log(arg);
            console.log(a1);
            console.log(a2);
        }
    })
}