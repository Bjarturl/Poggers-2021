<template>
  <b-container class="w-100 h-75 d-flex flex-column align-items-center pb-4">
    <h1 class="text-center">POGGERS 2021</h1>
    <b-row class="w-100 pb-5">
      <b-col
        class="selection-button"
        lg="5"
        md="11"
        @click="navigateTo('MostPopularData')"
        ><span>Virkastur</span> <img src="../assets/icons/fast-charge.png"
      /></b-col>
      <b-col
        class="selection-button"
        lg="5"
        md="11"
        @click="navigateTo('ReactionData')"
        ><span>Reactions</span> <img src="../assets/icons/reactions.png"
      /></b-col>
      <b-col
        class="selection-button"
        lg="5"
        md="11"
        @click="navigateTo('DataOverTime')"
        ><span>Tími dags</span> <img src="../assets/icons/clock.png"
      /></b-col>
      <b-col
        class="selection-button"
        lg="5"
        md="11"
        @click="navigateTo('CharacterCreation')"
        ><span>Berjast!</span> <img src="../assets/icons/swords.png"
      /></b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "PageSelection",
  methods: {
    navigateTo(loc) {
      this.$emit("navigate", loc);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.page-container {
  min-height: 90%;
}

.selection-button {
  background-color: #242424;
  color: white;
  border-radius: 35px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 10px;
  font-size: 24px;
  margin: 20px;
  padding: 10px;
  cursor: pointer;
  img {
    width: 150px;
    height: 150px;
  }
}
</style>
