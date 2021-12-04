<template>
  <div class="app-container">
    <Loading v-if="fetching" />
    <div v-else class="container">
      <b-container class="page-container">
        <component :is="pages[currPage]" />
      </b-container>
      <Pagination />
    </div>
  </div>
</template>

<script>
import { GET } from "./data/api";
import Loading from "./components/Loading.vue";
import Pagination from "./components/Pagination.vue";
import DataOverTime from "./templates/DataOverTime.vue";
import MostPopularData from "./templates/MostPopularData.vue";
export default {
  name: "App",
  components: {
    Loading,
    Pagination,
  },

  data() {
    return {
      fetching: false,
      pages: [MostPopularData, DataOverTime],
      currPage: 0,
    };
  },

  mounted() {
    this.getAllData();
  },

  methods: {
    async getAllData() {
      this.fetching = true;
      const data = await GET.allData();
      this.$store.years = data.years;
      this.$store.names = data.names;
      // setTimeout(() => {
      this.fetching = false;
      // }, 5000);
    },

    prevPage() {
      if (this.currPage > 0) {
        this.currPage -= 1;
      }
    },

    nextPage() {
      if (this.currPage < this.pages.length - 1) {
        this.currPage += 1;
      }
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
.app-container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: $primary;
  min-height: 100vh;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-end;
}

.page-container {
  background-color: $gray-400;
  min-height: 80%;
  padding: 40px;
  border: 3px solid $black;
  position: relative;
}
</style>
