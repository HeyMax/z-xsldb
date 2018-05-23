<template>
  <div class="hello">
    <h2 class="title">{{ msg }}</h2>
    <div class="input">
      <el-input class="text" v-model="keywords" placeholder="关键字,以','隔开" @keyup.enter="query" clearable></el-input>
      <el-button type="primary" @click="query">搜索</el-button>
    </div>
    <div class="details">关于 {{ this.keywords }} 共查询到 {{ size }} 条记录</div>
    <div>
        <div v-for="(item, index) in results" :key="item.Q">
          <div class="response">
            <div class="index"><b>{{index + 1}}:</b></div>
            <div class='test'>
              <div class="question"><b>Q:</b>{{item.Q}}</div>
              <!-- <hr style="height:1px;border:none;border-top:1px dashed #0066CC;" /> -->
              <div class="answer"><b>A:</b>{{item.A}}</div>
            </div>
          </div>
          <el-row>
           <hr style="height:3px;border:none;border-top:3px double #409EFF;" />
          </el-row>
        </div>
    </div>
    <span v-show="help" @click="showImg" class="help">救救孩子</span>
    <transition name="fade">
      <div v-show="support" class="detail">
        <div class="detail-wrapper clearfix">
          <!-- <img  class="img" src="../../static/cd.jpg"> -->
          <img class="img" src="../../static/czh.jpg">
        </div>
        <div class="detail-close" @click="closeImg">
          <i class="el-icon-close"></i>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'qq群问题搜索',
      keywords: '',
      size: 0,
      results: [],
      support: false,
      help: false
    }
  },
  methods: {
    query: function () {
      if (this.keywords === '') {
        this.help = false
        alert('请输入查询关键字!')
      } else {
        let form = {
          'keywords': this.keywords.split(',')
        }
        this.$http.post('http://172.20.16.164:7878/result/', form).then(Response => {
          let data = Response.data
          if (data.error_status === 1) {
            this.size = 0
            alert('未查询到数据')
          } else {
            this.help = true
            this.size = data.inventories.length
            this.results = data.inventories
          }
        })
      }
    },
    showImg: function () {
      this.support = true
    },
    closeImg: function () {
      this.support = false
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.hello
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  .title
    font-size 0px
  .input
    // display inline-block
    text-align center
    .text
      width 500px
      height 30px
  .details
    text-align center
  .response
    display table
    position relative
    .index
      display table-cell
      text-align center
      vertical-align: top
    .test
      display inline-block
      .question
        display block
      .answer
        display block
  .help
    position fixed
    bottom 0
    display block
    position relative
    text-align center
    font-size: 10px
    // margin-bottom 10px
    margin-left 40%
    margin-right 40%
  .detail
      position: fixed
      z-index: 100
      top: 0
      left: 0
      width: 100%
      height: 100%
      overflow: auto
      backdrop-filter: blur(10px)
      opacity: 1
      background: rgba(7, 17, 27, 0.8)
      &.fade-enter-active, &.fade-leave-active
        transition: all 0.5s
      &.fade-enter, &.fade-leave-active
        opacity: 0
        background: rgba(7, 17, 27, 0)
      .detail-wrapper
        width: 100%
        min-height: 100%
        text-align center
        .img
          width 300px
          height 500px
          padding-top 220px
      .detail-close
        position: relative
        width: 32px
        height: 32px
        margin: -80px auto 0 auto
        clear: both
        font-size: 32px
</style>
