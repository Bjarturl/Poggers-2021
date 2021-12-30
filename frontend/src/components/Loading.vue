<template>
  <div class="loading__container pb-5">
    <div class="loading">
      <div class="loading__character loading__character__ingvar">
        <div class="loading__fists loading__character__ingvar--fists">
          <img
            class="loading__fist loading__character__ingvar--fist1"
            src="../assets/hnefi.png"
          />
          <img
            class="loading__fist loading__character__ingvar--fist2"
            src="../assets/hnefi.png"
          />
        </div>
        <img
          class="loading__head loading__character__ingvar--head"
          src="../assets/ingvar.png"
        />
      </div>
      <div class="loading__character loading__character__arnie">
        <img
          class="loading__head loading__character__arnie--head"
          src="../assets/poggers_himself.png"
        />
      </div>
      <div class="loading__character loading__character__einar">
        <div class="loading__fists loading__character__einar--fists">
          <img
            class="loading__fist loading__character__einar--fist1"
            src="../assets/hnefi.png"
          />
          <img
            class="loading__fist loading__character__einar--fist2"
            src="../assets/hnefi.png"
          />
        </div>
        <img
          class="loading__head loading__character__einar--head"
          src="../assets/einar.png"
        />
      </div>
    </div>
    <span>{{ loadingText }}</span>
  </div>
</template>

<script>
export default {
  name: "Loading",
  components: {},
  data() {
    return {
      loadingText: "Sæki gögn",
      dots: 0,
    };
  },
  mounted() {
    setInterval(() => {
      if (this.dots === 3) {
        this.loadingText = "Sæki gögn";
        this.dots = 0;
      } else {
        this.loadingText += ".";
        this.dots += 1;
      }
    }, 500);
  },
};
</script>

<style lang="scss">
.loading {
  display: flex;
  padding: 30px;
  @include media-breakpoint-down(sm) {
    & {
      flex-direction: column;
    }
  }
  &__container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
    animation: BlinkingBackground 1s linear infinite;
    border-radius: 4px;
    span {
      padding-bottom: 10px;
      font-size: 32px;
      color: black;
      font-weight: bold;
    }
  }

  &__fists {
    position: absolute;
    top: 80px;
    z-index: 10;
  }
  &__fist {
    width: 60px;
    height: 80px;
    animation: MoveUpDown 0.5s linear infinite;
    &:nth-child(2n) {
      animation-delay: 0.2s;
    }
  }

  &__head {
    width: 180px;
    height: 180px;
  }
  &__character {
    position: relative;

    &__ingvar {
      margin-right: 40px;
      &--fists {
        transform: scaleX(-1);
        right: -50px;
      }
      &--head {
        animation: MoveUpDown 0.75s linear infinite;
      }
    }
    &__arnie {
      &--head {
        width: 160px;
        height: 160px;
        animation: FlipLeftRight 0.75s linear infinite;
      }
    }
    &__einar {
      margin-left: 40px;
      &--fists {
        left: -55px;
      }
      &--head {
        animation: MoveUpDown 0.5s linear infinite;
      }
    }
  }
}

@keyframes MoveUpDown {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0px);
  }
}

@keyframes BlinkingBackground {
  0% {
    background-color: #732641;
  }
  20% {
    background-color: #734126;
  }
  40% {
    background-color: #267341;
  }
  60% {
    background-color: #264173;
  }
  80% {
    background-color: #417326;
  }
  100% {
    background-color: #412673;
  }
}

@keyframes FlipLeftRight {
  0% {
    transform: translateX(-40px) rotate(15deg);
  }
  50% {
    transform: scaleX(-1) translateX(20px) rotate(30deg);
  }
  100% {
    transform: rotate(15deg);
  }
}
</style>
