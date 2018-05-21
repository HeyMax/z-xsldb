<template>
  <div class="hello">
    <h2 class="title">{{ msg }}</h2>
    <div class="input">
      <el-input class="text" v-model="keywords" placeholder="key words" @keyup.enter="query" clearable></el-input>
      <el-button type="primary" @click="query">搜索</el-button>
    </div>
    <div class="details">共查询到 {{ size }} 条记录</div>
    <div class="response">
      <ul>
        <li v-for="item in results" :key="item.Q">
          <h1>{{item.question}}</h1>
          <h2>{{item.answer}}</h2>
        </li>

      </ul>
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
      // if (this.keywords === '') {
      //   alert('请输入查询关键字!')
      // }
      // let url = 'http://172.20.16.160:7878/result/'
      // let url1 = 'http://172.31.251.31:8080'
      let form = {
        'keywords': ['cpu']
      }
      console.log(form)

      this.$http.post('http://172.20.16.160:7878', form).then(Response => {
        let data = Response.data
        console.log(data)
        if (data.error_status === 1) {
        } else {
          this.size = data.inventories.length
          this.results = data.inventories
          let qa = {'question': '', 'answer': ''}
          for (let i = 0; i < this.size; i++) {
            qa.question = data.inventories[i].Q
            qa.answer = data.inventories[i].A
            this.results.push(qa)
          }
        }
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.hello
  .title
    font-size 0px
  .input
    display inline-block
    align center
    .text
      width 500px
      height 30px
</style>
