<template>
  <div class="app-container">
    <Loading v-if="fetching" />
    <div v-else class="container">
      <b-container class="page-container">
        <component :is="pages[currPage]" />
      </b-container>
      <div class="app-options">
        <YearSelector />
        <Pagination />
      </div>
    </div>
  </div>
</template>

<script>
import { GET } from "./data/api";
import Loading from "./components/Loading.vue";
import Pagination from "./components/Pagination.vue";
import YearSelector from "./components/YearSelector.vue";
import CharacterCreation from "./templates/CharacterCreation.vue";
import DataOverTime from "./templates/DataOverTime.vue";
import MostPopularData from "./templates/MostPopularData.vue";
export default {
  name: "App",
  components: {
    Loading,
    Pagination,
    YearSelector,
  },

  data() {
    return {
      fetching: false,
      pages: [CharacterCreation, MostPopularData, DataOverTime],
      currPage: 0,
    };
  },

  mounted() {
    this.getAllData();
  },

  computed: {
    year() {
      return this.$store.year;
    },
  },

  watch: {
    year() {},
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
}

.app-options {
  display: flex;
  justify-content: space-between;
}

.page-container {
  background-color: $gray-400;
  min-height: 80%;
  padding: 40px;
  border: 3px solid $black;
  position: relative;
}
</style>
