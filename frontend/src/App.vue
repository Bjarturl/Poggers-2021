<template>
  <div class="app-container">
    <Loading v-if="fetching" />
    <b-container class="page-container" v-else>
      <component :is="pages[currPage]" />
      <div class="pagination">
        <div class="pagination__container">
          <b-iconstack
            rotate="180"
            font-scale="1.75"
            class="pagination__arrow"
            @click="prevPage"
            :class="currPage > 0 ? '' : 'pagination__arrow--disabled'"
          >
            <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
            <b-icon stacked icon="circle"></b-icon>
            <b-icon stacked icon="chevron-right"></b-icon>
          </b-iconstack>
          <span class="pagination__page">{{ currPage + 1 }}</span>
          <b-iconstack
            font-scale="1.75"
            class="pagination__arrow"
            @click="nextPage"
            :class="
              currPage < pages.length - 1 ? '' : 'pagination__arrow--disabled'
            "
          >
            <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
            <b-icon stacked icon="circle"></b-icon>
            <b-icon stacked icon="chevron-right"></b-icon>
          </b-iconstack>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
import { GET } from "./data/api";
import Loading from "./components/Loading.vue";
import DataOverTime from "./templates/DataOverTime.vue";
import MostPopularData from "./templates/MostPopularData.vue";
export default {
  name: "App",
  components: {
    Loading,
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
      this.fetching = false;
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
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: $primary;
}

.page-container {
  background-color: $gray-400;
  height: 80%;
  border: 3px solid $black;
  position: relative;
}

.pagination {
  position: absolute;
  right: -3px;
  bottom: -60px;
  &__page {
    font-size: 32px;
    margin-left: 5px;
    margin-right: 5px;
  }

  &__container {
    display: flex;
    align-items: center;
    border: 3px solid black;
    background-color: $gray-400;
    padding-left: 5px;
    padding-right: 5px;
  }

  &__arrow {
    cursor: pointer;
    &--disabled {
      cursor: auto;
      opacity: 0.75;
    }

    &:hover {
      opacity: 0.75;
      transition: opacity 0.3s ease;
    }
  }
}
</style>
