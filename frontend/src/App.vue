<template>
  <div id="app">
    <line-chart 
      :labels="['TEST', 'TEST2']"
      :lines="[{label: 'ye', data: [10,20]}]"
    />
  </div>
</template>

<script>
import LineChart from './components/LineChart.vue'
import { GET } from './data/api'

export default {
  name: 'App',
  components: {
    LineChart
  },
  mounted() {
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
