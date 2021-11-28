<template>
  <div id="app">
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import { GET } from './data/api'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  mounted() {
    this.getAllData()
    this.getMessagesByTime()
  },

  methods: {
    async getAllData() {
      const data = await GET.allData()
      this.$store.years = data.years
      this.$store.names = data.names
    },

    async getMessagesByTime() {
      const data = await GET.messagesByTimeData(this.$store.year)
      console.log(data);
    },

  }
} 
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
