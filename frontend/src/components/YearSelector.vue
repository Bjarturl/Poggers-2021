<template>
  <div class="year-selector">
    <div class="year-selector__container">
      <b-form-select v-model="$store.year" :options="$store.years" />
    </div>
  </div>
</template>

<script>
export default {
  name: "YearSelector",

  data() {
    return {};
  },

  methods: {},
};
</script>

<style lang="scss">
.year-selector {
  width: max-content;
  margin-top: -3px;

  &__container {
    display: flex;
    align-items: center;
    border: 3px solid black;
    background-color: $gray-400;
    padding: 5px;
  }
  select {
    background-color: $gray-400;
  }
}
</style>
