import argparse


class Argument():

    def __init__(self, base_path=None):
        parser = argparse.ArgumentParser(prog="wscan.py",
                                         usage="wscan.py [-u URL] [-f] [-m] [Extend options]",
                                         description="""
         A Fast & Simple web site scanner. 
        """, epilog="Example: \n\t wscan.py -u \"http://www.example.com/\" -f -m -v")

        parser.add_argument('-u', dest='url', action="store", required=True,
                            help='Target URL')

        parser.add_argument('-f', dest='fuzz', action="store_true",
                            help='\nFuzz target url with dictionary. ', default=False)

        parser.add_argument('-m', dest='map', action="store_true",
                            help='\nCrawl all URL on the target to get a map. ',
                            default=False)

        parser.add_argument('-max', dest="max_num", type=int,
                            help="""\nMax num of co-routine. [Default: 20]""", default=20)

        parser.add_argument('-b', dest="base",
                            help="""\nBase path for fuzzing.  e.g. "/cms/app" [Default: / ]""", default="/")

        parser.add_argument('-e', dest="extend",
                            help="""\nSuffix name used for fuzzing. [Default: php]""", default="php")

        parser.add_argument('-404', dest="not_found",
                            help="""\nCustomize a 404 identification, it'll be used as a keyword for searching text. """ + \
                                 """e.g. \"Not found\"""", default=None)

        parser.add_argument("-s", dest="static", action="store_true",
                            help="\nCrawl static resources when mapping target", default=False)

        parser.add_argument("--no-re", dest="no_re", action="store_true",
                            help="\nDon't redirect when requesting", default=False)

        detail_group = parser.add_mutually_exclusive_group()

        detail_group.add_argument('-v', dest="v", action="store_true",
                                  help="\nShow more detail", default=False)

        detail_group.add_argument('-vv', dest="vv", action="store_true",
                                  help="\nShow the most detailed details", default=False)

        self.args = parser.parse_args()
        self.args.base_path = base_path


<<<<<<< HEAD
    def get_args(self, arg_name=None):
        try:
            if arg_name:
                return eval("self.args." + arg_name)
        except Exception as e:
            pass
        return None
=======
    def get_args(self):
        return self.args
>>>>>>> b8a386b4b7a35f549d9671c8934a5617f5f70ffa


if __name__ == "__main__":
    # Argument()
    from bs4 import BeautifulSoup
    import re


    html = """



    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <script src="/Scripts/jquery.min.js"></script>
        <title>SSO 单点登录</title>
        <style>
            body {
                font-size: 14px;
                font-family: "Microsoft YaHei", 'Microsoft YaHei UI', Verdana, Helvetica, Sans-Serif;
                margin: 0;
            }
            
            .login-header {
                height: 50px;
                padding: 10px 20px;
            }
            
            .login-header img {
                height: 50px;
                width: auto;
            }
            
            .login-content {
                background: #3f98fc url(/Images/bg.png) no-repeat left center;
                background-size: auto 90%;
                height: 486px;
                margin: 0 auto;
                position: relative;
            }
            /*#loginForm {
            left: 45%;
            margin-top: -30px;
            position: absolute;
            right: 0;
        }*/
            
            .login-form {
                margin: 0 auto;
                /*width: 360px;*/
                width: 100%;
            }
            
            .login-form-header {
                background: transparent url(/Images/bv.png) no-repeat left center;
                background-size: 100%;
                height: 30px;
            }
            
            .login-form-body {
                /*background-color: #f1f1f1;*/
                margin: 0 auto;
                padding: 1px 24px 24px;
                width: 260px;
            }
            
            .login-form-body h3 {
                margin-top: 0;
                text-align: center;
            }
            
            .login-form-body hr {
                border-bottom: 0 none;
                border-top: 1px solid #ccc;
            }
            
            .login-form-body p {
                color: #b4b4b4;
                text-align: center;
            }
            
            .icon-left {
                /*border-bottom-left-radius: 4px;
            border-top-left-radius: 4px;*/
                border-right: 1px solid #bdbdbd;
                /*border-right: 0;*/
                height: 38px;
                /*padding: 5px;*/
                position: absolute;
                left: 1px;
                top: 1px;
                width: 38px;
                background-color: #f3f3f3 !important;
            }
            
            .icon-user {
                background: transparent url(/Images/zhanghu.png) no-repeat center;
            }
            
            .icon-password {
                background: transparent url(/Images/mima.png) no-repeat center;
            }
            
            .login-reset-content .icon-password {
                background: transparent url(/Images/yanzhengma.png) no-repeat center;
            }
            
            .login-input {
                border: 1px solid #bdbdbd;
                /*border-radius: 4px;*/
                padding: 4px 8px 4px 48px;
                height: 30px;
                box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset;
                transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
                width: 78%;
            }
            
            .login-input:focus {
                border-color: #66afe9;
                box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px rgba(102, 175, 233, 0.6);
                outline: 0 none;
            }
            
            .login-input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0px 1000px white inset;
            }
            
            .login-input:focus:-webkit-autofill {
                -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px rgba(102, 175, 233, 0.6), 0 1px 0px 1000px white inset;
            }
            
            .login-btn {
                background-color: #ffa800;
                /*f19457*/
                /*border: 1px solid #d9d9d9;*/
                /*border-radius: 4px;*/
                border: none;
                color: #fff;
                cursor: pointer;
                padding-bottom: 10px;
                padding-top: 10px;
                text-align: center;
                width: 100%;
            }
            
            .login-btn:hover {
                background-color: #ff9900;
                /*f1853e;*/
            }
            
            .row-mt-10 {
                margin-top: 10px;
            }
            
            .row-mt-20 {
                margin-top: 20px;
            }
            
            .login-footer {
                text-align: center;
            }
            
            .login-footer span {
                margin-left: 20px;
            }
            
            .login_error {
                color: #e12f2f;
            }
            
            .fade {
                opacity: 0;
                -webkit-transition: opacity .15s linear;
                -o-transition: opacity .15s linear;
                transition: opacity .15s linear;
            }
            
            .fade.in {
                opacity: 1;
            }
            
             :after,
             :before {
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box;
            }
            
            .popover {
                position: absolute;
                top: 0;
                left: 0;
                z-index: 1060;
                display: none;
                max-width: 276px;
                padding: 1px;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                font-size: 14px;
                font-style: normal;
                font-weight: 400;
                line-height: 1.42857143;
                text-align: left;
                text-align: start;
                text-decoration: none;
                text-shadow: none;
                text-transform: none;
                letter-spacing: normal;
                word-break: normal;
                word-spacing: normal;
                word-wrap: normal;
                white-space: normal;
                background-color: #fff;
                -webkit-background-clip: padding-box;
                background-clip: padding-box;
                border: 1px solid #ccc;
                border: 1px solid rgba(0, 0, 0, .2);
                border-radius: 6px;
                -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
                box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
                line-break: auto;
            }
            
            .popover.bottom {
                margin-top: 10px;
            }
            
            .popover.bottom>.arrow {
                top: -11px;
                left: 50%;
                margin-left: -11px;
                border-top-width: 0;
                border-bottom-color: #999;
                border-bottom-color: rgba(0, 0, 0, .25);
            }
            
            .popover>.arrow {
                border-width: 11px;
            }
            
            .popover>.arrow,
            .popover>.arrow:after {
                position: absolute;
                display: block;
                width: 0;
                height: 0;
                border-color: transparent;
                border-style: solid;
            }
            
            .popover>.arrow,
            .popover>.arrow:after {
                position: absolute;
                display: block;
                width: 0;
                height: 0;
                border-color: transparent;
                border-style: solid;
            }
            
            .popover>.arrow:after {
                content: "";
                border-width: 10px;
            }
            
            .popover.bottom>.arrow:after {
                top: 1px;
                margin-left: -10px;
                content: " ";
                border-top-width: 0;
                border-bottom-color: #fff;
            }
            
            .popover-title {
                font-family: inherit;
                font-weight: 500;
                line-height: 1.1;
                color: inherit;
                padding: 8px 14px;
                margin: 0;
                font-size: 14px;
                background-color: #f7f7f7;
                border-bottom: 1px solid #ebebeb;
                border-radius: 5px 5px 0 0;
            }
            
            .popover-content {
                padding: 9px 14px;
            }
            
            .popover-content img {
                width: 150px;
            }
            
            #yidongduan {
                color: red;
                /*text-decoration: none;*/
                position: relative;
            }
            
            .popover {
                display: none;
            }
            
            #yidongduan:hover .popover {
                display: block;
            }
            
            .f-red {
                color: #f00;
            }
            
            .f-grey {
                color: #363636;
            }
            
            .login-box {
                position: absolute;
                top: 42px;
                right: 18%;
                border-radius: 4px;
                box-shadow: 0 0 10px #fff;
                font-size: 14px;
                /*line-height: 50px;*/
                width: 346px;
                height: 390px;
                background: #fff;
            }
            
            .login-tabs {
                list-style: none;
                padding: 0;
                margin: 0;
                border-radius: 4px 4px 0 0;
                overflow: hidden;
                background: #f0f4f7;
                font-size: 20px;
            }
            
            .login-tabs li {
                float: left;
                width: 50%;
            }
            
            .login-tab {
                height: 60px;
                display: block;
                line-height: 60px;
                text-align: center;
                color: #616161;
                text-decoration: none;
            }
            
            .login-tab.active {
                pointer-events: none;
                background: #fff;
                color: #1b82cd;
            }
            
            .login-tab-content {
                display: none;
                text-align: center;
            }
            
            .login-tab-content.active {
                display: block;
            }
            
            .login-tab-footer {
                line-height: 52px;
                position: absolute;
                bottom: 0;
                padding: 0 10px;
                width: 100%;
                box-sizing: border-box;
                font-size: 16px;
            }
            
            .login-tab-footer .register {
                float: right;
            }
            
            p {
                margin: 0;
            }
            
            .code-box {
                width: 212px;
                height: 212px;
                margin: 10px auto;
                overflow: hidden;
            }
            
            #codeIframe {
                margin: -180px -500px;
                height: 600px;
            }
            
            .login-reset-header {
                list-style: none;
                padding: 0;
                margin: 0;
                border-radius: 4px 4px 0 0;
                overflow: hidden;
                background: #f0f4f7;
                font-size: 20px;
                height: 60px;
                border-bottom: 1px solid #c6d3dc;
                text-align: center;
                position: relative;
            }
            
            .login-reset-header p {
                height: 60px;
                line-height: 60px;
                color: #1b82cd;
                background: #fff;
            }
            
            .login-reset-header .login-backLogin {
                position: absolute;
                left: 7px;
                top: 5px;
                cursor: pointer;
            }
            
            .login-reset-content {
                margin: 0 auto;
                padding: 1px 24px 24px;
                width: 260px;
            }
            
            .login-reset-content p {
                color: red;
                text-align: center;
            }
            
            .login-reset-content .getCodeBtn {
                height: 40px;
                width: 112px;
                border: 1px solid #bdbdbd;
                border-left: none;
                color: #fff;
                background-color: #e2e2e2;
                position: absolute;
                right: 0;
                top: 0;
                cursor: pointer;
            }
            
            .login-reset-footer {
                position: absolute;
                bottom: 18px;
                right: 20px;
                color: #ff0000;
            }
            
            .getCodeBtn.active {
                background-color: #3f87fc
            }
            
            .login-tab-getPassword {
                position: absolute;
                right: 45px;
                color: #1b82cd;
                cursor: pointer;
            }
            
            .login-tab-getPassword a {
                text-decoration: underline;
            }
            
            .login-registered {
                color: #f00;
                font-size: 16px;
            }
            
            .login-reset-foo input::-webkit-outer-spin-button,
            input::-webkit-inner-spin-button {
                -webkit-appearance: none !important;
                margin: 0;
            }
            
            input[type="number"] {
                -moz-appearance: textfield;
            }
            
            .hide {
                display: none;
            }
        </style>
    </head>


    <body onload="javascript:if (top.location !== self.location) {top.location=self.location;};">
        <div class="login-header">
            <img src="/Images/logo.png" alt="" />
        </div>
        <div class="login-content">
            <div class="login-box login-normal">
                <ul class="login-tabs">
                    <li><a href="javascript:;" class="login-tab" data-target="tab-code">二维码登录</a></li>
                    <li><a href="javascript:;" class="login-tab active" data-target="tab-form">账户登录</a></li>
                </ul>
                <div class="login-tab-contents">
                    <div class="login-tab-content" id="tab-code">
                        <div class="code-box"><iframe id="codeIframe"></iframe></div>
                        <p class="f-red">打开口袋助理 扫描二维码</p>
                        <p class="f-grey">手机扫描，安全登录</p>
                    </div>
                    <div class="login-tab-content active" id="tab-form">
                        <form name="loginForm" method="post" action="login.aspx?appcode=1005&amp;returnUrl=" id="loginForm">
<div>
<input type="hidden" name="__LASTFOCUS" id="__LASTFOCUS" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTcyNzExMTU3MGRkkPkm23TKIfJ85k3EFwA5OGEGekqdiIIHjP8tzs2awcg=" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['loginForm'];
if (!theForm) {
    theForm = document.loginForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=2uDjE1N9xh_c5-DMaUvKitL0chnjY3iqsbA0O8HKv1aODTxKZX7l2G32VymLz-URzSA9mTTIH8w7ce2rOKWNt2DPOyqXmK9DozNYqI0PsWc1&amp;t=635145251460000000" type="text/javascript"></script>


<script src="/WebResource.axd?d=rYqqd9rrhYVHNZzE3kr8M5sh87JSZKL9fdMvi7hk_SOeVpITsWKgODrMCczDxLiV3ZdIjZqzSqqcRNiOOjIre8O-dMCHOHEOe7GdbsNKHY41&amp;t=635145251460000000" type="text/javascript"></script>
<div>

	<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
	<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAASJd12Yo/caMd6c0wvtHudPY3plgk0YBAefRz3MyBlTcHY2+Mc6SrnAqio3oCKbxYainihG6d/Xh3PZm3b5AoMQ1lyLgUwXZR0xlkk2qz5Q8snSKpRWdVizOybTKko9EoA=" />
</div>
                            <div class="login-form">
                                <!--<div class="login-form-header"></div>-->
                                <div class="login-form-body">
                                    <div>
                                        <!--<h3>集团门户</h3>
                                    <hr />-->
                                        <p style="line-height: 50px;">规范、高效、整合、先进的协同体验</p>
                                    </div>
                                    <div style="position: relative;">
                                        <i class="icon-left icon-user"></i>
                                        <input name="txtUserName" type="text" id="txtUserName" class="login-input" />
                                    </div>
                                    <div class="row-mt-10" style="position: relative;">
                                        <i class="icon-left icon-password"></i>
                                        <input name="txtPassword" type="password" maxlength="30" id="txtPassword" class="login-input" />
                                    </div>
                                    <div class="row-mt-10">
                                        
                                    </div>
                                    <div class="row-mt-20">
                                        <input type="submit" name="btnLogin" value="登录" id="btnLogin" class="login-btn" />
                                    </div>
                                    <!--<div class="row-mt-20">
                                    <a href="" target="_blank" id="yidongduan">
                                        移动端门户
                                        <div class="popover fade bottom in" role="tooltip" id="moa" style="top: 20px; left: 0;">
                                            <div class="arrow" style="left: 15%;"></div>
                                            <h3 class="popover-title">扫一扫下载专享版MOA</h3>
                                            <div class="popover-content"><img src="/Images/sfbeta.png"></div>
                                        </div>
                                    </a>
                                </div>-->
                                </div>
                            </div>
                        

<script type="text/javascript">
//<![CDATA[
WebForm_AutoFocus('txtUserName');//]]>
</script>
</form>
                        <div class="login-tab-getPassword">
                            <a>忘记密码？</a>
                        </div>
                    </div>
                </div>

                <div class="login-tab-footer">
                    <a href="javascript:;" target="_blank" id="yidongduan">
                    专享版MOA
                    <div class="popover fade bottom in" role="tooltip" id="moa" style="top: 20px; left: 0;">
                        <div class="arrow" style="left: 15%;"></div>
                        <h3 class="popover-title">扫一扫下载专享版MOA</h3>
                        <div class="popover-content"><img src="/Images/sfbeta.png"></div>
                    </div>
                </a>
                    <div class="register"><a id="toRegister" href="javascript:void(0)" class="f-red">注册账号 >></a></div>
                </div>
            </div>
            <div class="login-box login-reset hide">
                <div class="login-reset-header">
                    <img src="/Images/back.png" class="login-backLogin">
                    <p>忘记密码</p>
                </div>
                <div class="login-reset-content">
                    <div>
                        <p style="line-height: 50px;">请在MOA查询验证码和密码</p>
                    </div>
                    <div style="position:relative;">
                        <i class="icon-left icon-user"></i>
                        <input type="number" placeholder="请输入工号" class="login-input login-getId">
                    </div>
                    <div style="position:relative;" class="row-mt-10">
                        <i class="icon-left icon-password"></i>
                        <input type="text" placeholder="请输入验证码" maxlength="6" class="login-input login-writeCode" style="width:90px">
                        <button class="getCodeBtn">获取MOA验证码</button>
                    </div>
                    <div class="row-mt-20">
                        <input type="submit" value="重置密码" class="login-btn resetPassword">
                    </div>
                </div>
                <div class="login-reset-footer">
                    <a class="login-registered" href="http://200.200.4.131:8001/html/register.html">注册账号>></a>
                </div>
            </div>
        </div>
        <div class="login-footer">
            <p>&copy;
                2018<span>深信服科技股份有限公司版权所有</span></p>
        </div>
        <script src="/Scripts/APIConfig.js?v=03" type="text/javascript"></script>
        <script>
            //var API = 'http://ssebeta.sangfor.com/Ashx',
                // var API = 'http://200.200.3.33:8066/Ashx',
                //allowOrigin = ['http://ssebeta.sangfor.com', 'http://200.200.3.33:8066'];
            // var yidongduan = document.getElementById('yidongduan');
            // var moa = document.getElementById('moa');
            // yidongduan.onmouseover = function(){
            //     moa.style.display = 'block';
            // }
            function getJSONP(url, callback) {
                if (!url) {
                    return;
                }
                var a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']; //定义一个数组以便产生随机函数名  
                var r1 = Math.floor(Math.random() * 10);
                var r2 = Math.floor(Math.random() * 10);
                var r3 = Math.floor(Math.random() * 10);
                var name = 'getJSONP' + a[r1] + a[r2] + a[r3];
                var cbname = 'getJSONP.' + name; //作为jsonp函数的属性  
                if (url.indexOf('?') === -1) {
                    url += '?jsonp=' + cbname;
                } else {
                    url += '&jsonp=' + cbname;
                }
                // url += '/' + cbname;  
                var script = document.createElement('script');
                //定义被脚本执行的回调函数  
                getJSONP[name] = function(e) {
                    try {
                        //alert(e.name);  
                        　　　　　　　　
                        callback && callback(e);
                    } catch (e) {
                        //  
                    } finally {
                        //最后删除该函数与script元素  
                        delete getJSONP[name];
                        script.parentNode.removeChild(script);
                    }

                }
                script.src = url;
                document.getElementsByTagName('head')[0].appendChild(script);
            }
            document.addEventListener('click', function(e) {
                e = e || window.event;
                var ele = e.target;
                if (ele.classList.contains('login-tab')) {
                    console.log(document.getElementsByClassName('active'))
                        // Array.prototype.map.call(document.getElementsByClassName('active'), function(el) {
                        //     el.classList.remove('active');
                        // });
                    Array.prototype.slice.call(document.getElementsByClassName('active')).forEach(function(el) {
                        el.classList.remove('active');
                    });
                    ele.classList.add('active');
                    // console.log(document.getElementById(e.target.getAttribute('data-target')))
                    document.getElementById(ele.getAttribute('data-target')).classList.add('active');
                }
            });

            function getCode() {
                getJSONP(API + '/ScanGetUrl.ashx', function(data) {
                    // try {
                    // console.log(document.getElementById('codeIframe'))
                    document.getElementById('codeIframe').src = data.url;
                    // } catch (error) {

                    // }
                });
            }

            function LoginSuccess(data) {
                var txtUserName = document.getElementById('txtUserName');
                var txtPassword = document.getElementById('txtPassword');
                var otxtUserName = txtUserName.value;
                var otxtPassword = txtPassword.value;
                txtUserName.value = data.loginname;
                txtPassword.value = data.password;
                document.getElementById('btnLogin').click();
                setTimeout(function() {
                    txtUserName.value = otxtUserName;
                    txtPassword.value = otxtPassword;
                }, 0);
            }

            function receiveMessage(e) {
                if (allowOrigin.indexOf(e.origin) !== -1) {
                    if (e.data) {
                        if (e.data.state == 1) {
                            LoginSuccess(e.data);
                        } else if (e.data.state == -1) {
                            getCode();
                            alert('登录失败：内部错误，请重新扫码或联系管理员！');
                        } else if (e.data.state == 0) {
                            getCode();
                            alert('登录失败：该用户或账号不存在，请注册账号！');
                        }
                    }
                }
            }
            //重置密码
            $(function() {
                // var api;
                // if (document.location.host === '200.200.0.133:8060') {
                //     api = 'http://200.200.0.133:8001/Ashx';
                // } else if (document.location.host === '200.200.4.131:8060') {
                //     api = 'http://200.200.4.131:8001/Ashx';
                // } else {
                //     api = 'http://200.200.3.33:8066/Ashx';
                // }


                function resetPassword() {
                    var number = 60;

                    $('.login-getId').keyup(function() {
                        var userId = $(this).val();
                        var checkREGEXP = /^\d{5}$|^\d{9}$/;
                        if (checkREGEXP.test(userId)) {
                            //确认工号能够使用
                            // $.ajax({
                            //     url: '',
                            //     type: '',
                            //     success: function() {

                            //     }
                            // })
                            $('.getCodeBtn').addClass('active');
                        } else {

                            $('.getCodeBtn').removeClass('active');
                            return
                        }

                    });
                    //"http://200.200.4.131:8001/html/register.html" 跳转注册页面
                    $('#toRegister').on('click', function() {
                        window.open(registerApi + '/html/register.html');
                    })
                    //点击获取验证码
                    $('.login-reset-content').on('click', '.getCodeBtn', function() {
                            var self = this;
                            if ($(this).html() != '获取MOA验证码' || !$(this).hasClass('active')) return;
                            $(this).html('验证码(' + number + ')');
                            $.ajax({
                                url: api + '/SendMoaIdetity.ashx?gh=' + $('.login-getId').val(),
                                type: 'get',
                                dataType: 'jsonp',
                                success: function(data) {
                                    console.log(data);

                                    if(data == 1) {
                                        
                                        time = setInterval(function() {
                                            number += -1;
                                            $(self).html('验证码(' + number + ')');
                                            if (number == -1) {
                                                clearInterval(time);
                                                $(self).html('获取MOA验证码');
                                                number = 60;
                                            }
                                        }, 1000)
                                    } else {
                                        $(self).html('获取MOA验证码');
                                        alert('获取验证码失败,请重新获取');

                                    }
                                    
                                },
                                error: function() {
                                    alert('发送验证码失败')
                                }

                            })


                        })
                        //返回
                    $('.login-reset').on('click', '.login-backLogin', function() {
                        $('.login-normal').removeClass('hide');
                        $('.login-reset').addClass('hide');
                    })
                    $('.login-tab-getPassword').on('click', 'a', function() {
                        $('.login-normal').addClass('hide');
                        $('.login-reset').removeClass('hide');
                    })
                    $('.resetPassword').on('click', function() {
                        if($('.login-getId').val() && $('.login-writeCode').val()) {
                            $.ajax({
                                url: api + '/ForgretPassword.ashx?gh=' + $('.login-getId').val() + '&code=' + $('.login-writeCode').val(),
                                dataType: 'jsonp',
                                type: 'get',
                                success: function(data) {
                                    if(data == 1) {
                                        alert('重置成功！');
                                        $('.login-backLogin').trigger('click');
                                        $('#txtUserName').val($('.login-getId').val());
                                    } else {
                                        alert('验证码错误，请重新输入!');
                                    }
                                    
                                },
                                error: function() {
                                    alert('验证码错误!');

                                }
                            })
                        } else {
                            alert('请填写验证码')
                        }
                        
                    })

                }
                resetPassword();

            });


            window.addEventListener("message", receiveMessage, false);
            getCode();
        </script>
    </body>

    </html>
    
    """
    soup = BeautifulSoup(html, "html.parser")
    # regexp = re.compile("404 - 找不到文")
    # print(soup.find(text=regexp))
    for i in soup.find_all('script'):
        print(i)
        print(i.get('src'))
