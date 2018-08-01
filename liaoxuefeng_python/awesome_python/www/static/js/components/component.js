//分页组件
Vue.component('page-component',{

    props : ['page'],
    template: '<ul class="uk-pagination">\n' +
    '        <li class="uk-disabled" :class="{\'uk-active\': page.has_previous}">\n' +
    '            <template v-if="page.has_previous">\n' +
    '                <a @click="gotoPage(page_pre)"><i class="uk-icon-angle-double-left"></i> 上一页</a>\n' +
    '            </template>\n' +
    '            <template v-else>\n' +
    '                <span><i class="uk-icon-angle-double-left"></i> 上一页 </span>\n' +
    '            </template>\n' +
    '        </li>\n' +
    '        <li v-for="pages in page.page_count" v-if="pages < 11" class="uk-active" :class="{\'uk-disabled\': pages!=page.page_index}">\n' +
    '            <template v-if="pages==page.page_index">\n' +
    '                <span v-text="pages"></span>\n' +
    '            </template>\n' +
    '            <template v-else>\n' +
    '                <a v-text="pages" @click="gotoPage(pages)"></a>\n' +
    '            </template>\n' +
    '        </li>\n' +
    '        <li class="uk-disabled" :class="{\'uk-active\': page.has_next}">\n' +
    '            <template v-if="page.has_next">\n' +
    '                <a @click="gotoPage(page_next)"> 下一页 <i class="uk-icon-angle-double-right"></i></a>\n' +
    '            </template>\n' +
    '            <template v-else>\n' +
    '                <span> 下一页 <i class="uk-icon-angle-double-right"></i>  </span>\n' +
    '            </template>\n' +
    '        </li>\n' +
    '    </ul>',
    methods: {
        gotoPage: function (page) { gotoPage(page) }
    },
    computed:{
        page_pre:function () {
            if (this.page.has_previous) { return (this.page.page_index - 1) }
            return 0;
        },
        page_next:function () {
            if (this.page.has_next) { return (this.page.page_index + 1) }
            return 0;
        }
    }
});
