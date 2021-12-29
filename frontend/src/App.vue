<template>
  <div class="app-container">
    <Loading v-if="fetching" />
    <div v-else class="main-container">
      <b-container class="page-container">
        <component :is="pages[currPage]" />
      </b-container>
      <div class="app-options">
        <YearSelector v-on:update="updateYear" />
        <Pagination :pages="pages.length" v-on:navigate="updatePage" />
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
import ReactionData from "./templates/ReactionData.vue";
import Timeline from "./templates/Timeline.vue";
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
      pages: [
        CharacterCreation,
        Timeline,
        ReactionData,
        MostPopularData,
        DataOverTime,
      ],
      currPage: this.$store.currPage,
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
    updatePage(page) {
      this.$store.currPage = page;
      this.currPage = page;
    },
    updateYear(year) {
      this.$store.year = year;
      this.getAllData();
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
  background-image: url("./assets/poggers_himself.jpg");
  background-size: 200px 200px;
  height: 100vh;
}

.main-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 80vh;
  width: 100%;
}

.app-options {
  display: flex;
  justify-content: center;
}

.page-container {
  background-color: $gray-400;
  min-height: 80%;
  width: 90%;
  min-width: 90%;
  padding: 40px;
  border: 3px solid $black;
  position: relative;
  overflow: scroll;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  &::-webkit-scrollbar {
    display: none;
  }
}
</style>
