<template>
  <div class="year-selector">
    <div class="year-selector__container">
      <b-form-select
        :value="$store.year"
        @change="updateYear"
        :options="$store.years"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "YearSelector",

  data() {
    return {};
  },

  methods: {
    updateYear(year) {
      this.$emit("update", year);
    },
  },
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
