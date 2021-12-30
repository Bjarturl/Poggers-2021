<template>
  <div>
    <div class="app-container">
      <video
        class="video-bg"
        autoplay
        loop
        muted
        src="PoggersBG.mp4"
        type="video/mp4"
      ></video>
      <div class="main-container" v-if="fetching">
        <Loading />
      </div>
      <div v-else class="main-container">
        <b-container class="page-container">
          <component
            v-if="buttonPage"
            :is="buttonPage"
            v-on:toggling="togglePagination"
          />
          <component
            v-else
            :is="pages[currPage]"
            v-on:navigate="handleNavigation"
          />
          <div class="app-options">
            <Pagination
              v-if="!paginationHidden"
              :pages="pages.length"
              :btn-page="buttonPage !== null"
              v-on:clear="clearButtonPage"
              v-on:navigate="updatePage"
              v-on:update="updateYear"
            />
          </div>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
import { GET } from "./data/api";
import Loading from "./components/Loading.vue";
import Pagination from "./components/Pagination.vue";
import CharacterCreation from "./templates/CharacterCreation.vue";
import DataOverTime from "./templates/DataOverTime.vue";
import MostPopularData from "./templates/MostPopularData.vue";
import ReactionData from "./templates/ReactionData.vue";
import Timeline from "./templates/Timeline.vue";
import Video from "./templates/Video.vue";
import PageSelection from "./templates/PageSelection.vue";
export default {
  name: "App",
  components: {
    Loading,
    Pagination,
  },

  data() {
    return {
      fetching: false,
      pages: [Video, Timeline, PageSelection],
      buttonPages: {
        ReactionData: ReactionData,
        MostPopularData: MostPopularData,
        DataOverTime: DataOverTime,
        CharacterCreation: CharacterCreation,
      },
      currPage: this.$store.currPage || 0,
      buttonPage: null,
      paginationHidden: false,
    };
  },

  mounted() {
    this.getAllData();
    this.currPage = this.$store.currPage;
  },

  methods: {
    async getAllData() {
      this.fetching = true;
      const data = await GET.allData();
      this.$store.years = data.years.sort((y1, y2) => {
        if (!isNaN(y1) && !isNaN(y2)) {
          return parseInt(y1) - parseInt(y2);
        } else if (isNaN(y1) && !isNaN(y2)) {
          return 1;
        } else if (!isNaN(y1) && isNaN(y2)) {
          return -1;
        }
        return 0;
      });
      this.$store.names = data.names;
      setTimeout(() => {
        this.fetching = false;
      }, 3000);
    },

    clearButtonPage() {
      this.buttonPage = null;
    },

    togglePagination(val) {
      this.paginationHidden = val;
    },

    handleNavigation(loc) {
      this.loc = loc;
      this.buttonPage = this.buttonPages[loc];
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
@font-face {
  font-family: "Roboto black";
  src: url("./assets/fonts/Roboto/Roboto-Black.ttf");
}

@font-face {
  font-family: "Roboto medium";
  src: url("./assets/fonts/Roboto/Roboto-Medium.ttf");
}

@font-face {
  font-family: "Fredoka one";
  src: url("./assets/fonts/Fredoka_One/FredokaOne-Regular.ttf");
}
body {
  font-family: "Roboto black";
  overflow: hidden;
}
@import "~@/assets/scss/vendors/bootstrap-vue/index";
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-size: 200px 200px;
  z-index: 2;
  height: 100vh;
  @include media-breakpoint-down(sm) {
    & {
      padding-top: 70px;
      padding-bottom: 70px;
    }
  }
}

.video-bg {
  position: absolute;
  top: 0;
  width: 100%;
  z-index: -1;
  object-fit: fill;
  height: 100%;
}

.main-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 80vh;
  width: 100%;
}

.app-options {
  position: fixed;
  margin-bottom: 100px;
  width: 85%;
  @include media-breakpoint-down(sm) {
    & {
      margin-bottom: 10px;
      width: 100%;
    }
  }
  bottom: 0;
}

.page-container {
  background-color: rgba(black, 0.8);
  border-radius: 35px;
  color: white;
  width: 90%;
  max-height: 100vh;
  height: 90vh;
  min-width: 90%;
  padding: 40px 40px 20px 40px;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  @include media-breakpoint-down(sm) {
    & {
      width: 100%;
      padding: 5px;
    }
  }
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  &::-webkit-scrollbar {
    display: none;
  }
}
</style>
