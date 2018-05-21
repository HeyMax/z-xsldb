<template>
  <div class="hello">
    <h2 class="title">{{ msg }}</h2>
    <div class="input">
      <el-input class="text" v-model="keywords" placeholder="关键字,以','隔开" @keyup.enter="query" clearable></el-input>
      <el-button type="primary" @click="query">搜索</el-button>
    </div>
    <div class="details">关于 {{ this.keywords }} 共查询到 {{ size }} 条记录</div>
    <div>
        <div class="response" v-for="(item, index) in results" :key="item.Q">
          <div class="question">{{index + 1}}:{{item.Q}}</div>
          <!-- <hr style="height:1px;border:none;border-top:1px dashed #0066CC;" /> -->
          <div> </div>
          <div class="answer">{{item.A}}</div>
          <el-row>
           <hr style="height:3px;border:none;border-top:3px double #409EFF;" />
          </el-row>
        </div>
    </div>
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
      results: []
    }
  },
  methods: {
    query: function () {
      if (this.keywords === '') {
        alert('请输入查询关键字!')
      } else {
        this.result = []
        // let url = 'http://172.20.16.160:7879/result/'
        // let url1 = 'http://172.31.251.31:8080'
        let form = {
          'keywords': this.keywords.split(',')
        }
        console.log(form)

        this.$http.post('http://172.20.16.160:7879/result/', form).then(Response => {
          let data = Response.data
          console.log(data)
          if (data.error_status === 1) {
            alert('未查询到数据')
          } else {
            this.size = data.inventories.length
            this.results = data.inventories
          }
          console.log(this.results)
        })
      }
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
    display block
    margin 100px,20px,100px,20px
    align left
</style>
