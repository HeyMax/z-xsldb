<template>
  <div id="app">
    <div class="head">
    <img class="img" src="http://www.zstack.io/templets/default/images/top/Logo_Horizontal_addtitle.png">
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.head
  text-align: center
  color: #2c3e50
  margin-top: 60px
</style>
