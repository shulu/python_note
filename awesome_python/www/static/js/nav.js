function initNAV()
{
    var nav = new Vue({
        el:'#nav',
        data:{
            navs: [
                {nav_title:'日志',id:'blogs', nav_url:'/', data_url:'blogs'},
                {nav_title:'每周推送',id:'post_weekly', nav_url:'/acfun/focus', data_url:'acfun_focus'},
                {nav_title:'金光布袋戏',id:'jinguang', nav_url:'/jinguang', data_url:'jinguang'}
            ],
            now_index : 0

        },
        methods:{
            navClick:function(index){
                this.now_index=index;
            }
        }
    });
}
initNAV();
