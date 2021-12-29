<template>
  <b-container class="msgs-container" v-if="!fetching">
    <h1>{{ msgs }} skilaboð send {{ yearText }}</h1>
    <h1>{{ imgs }} myndir sendar {{ yearText }}</h1>
  </b-container>
  <Loading v-else />
</template>

<script>
import { GET } from "../data/api";
import Loading from "../components/Loading.vue";
export default {
  name: "Timeline",
  components: {
    Loading,
  },

  props: {},

  async mounted() {
    this.fetching = true;
    await GET.allTimeData(this.$store.year).then(
      function (data) {
        this.imgs = data[0]["heildarfjöldi_mynda"][0]["Heildarfjöldi mynda"];
        this.msgs =
          data[1]["heildarfjöldi_skilaboða"][0]["Heildarfjöldi skilaboða"];
      }.bind(this)
    );
    this.fetching = false;
  },

  data() {
    return {
      msgs: 0,
      imgs: 0,
      fetching: false,
    };
  },

  computed: {
    yearText() {
      if (this.$store.year === "Frá byrjun") {
        return "frá upphafi";
      }
      return "á árinu " + this.$store.year;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.msgs-container {
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}
</style>
