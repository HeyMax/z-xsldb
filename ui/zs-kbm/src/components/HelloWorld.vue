<template>
  <div class="hello">
    <h2 class="title">{{ msg }}</h2>
    <div class="input">
      <el-input class="text" v-model="keywords" placeholder="key words" @keyup.enter="query" clearable></el-input>
      <el-button type="primary" @click="query">搜索</el-button>
    </div>
    <div class="details">共查询到{{ size }}条记录</div>
    <div class="response">
      <ul>
        <li ></li>
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
      size: 0
    }
  },
  methods: {
    query: function () {
      // if (this.keywords === '') {
      //   alert('请输入查询关键字!')
      // }
      this.$http.get('http://172.31.251.31:9999/').then(Response => {
        let data = Response.data
        if (data.error_status === 1) {
        } else {
          this.size = data.inventories.length
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
