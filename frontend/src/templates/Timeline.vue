<template>
  <b-container class="w-100 h-75 timeline" v-if="!fetching">
    <h1 class="text-center">POGGERS 2021</h1>
    <div class="pyro h-100" v-if="!fetching">
      <div class="before"></div>
      <div
        class="
          d-flex
          flex-column
          justify-content-around
          h-100
          align-items-center
          text-center
        "
      >
        <h1>
          <span class="text-primary">{{ msgs }}</span> skilaboð send
          {{ yearText }}
        </h1>
        <h1>
          <span class="text-danger">{{ imgs }}</span> myndir sendar
          {{ yearText }}
        </h1>
      </div>

      <div class="after"></div>
    </div>
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
    setTimeout(() => {
      this.fetching = false;
    }, 2000);
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
<style lang="scss">
.page-container {
  min-height: 90%;
}
$particles: 50;
$width: 500;
$height: 500;

// Create the explosion...
$box-shadow: ();
$box-shadow2: ();
@for $i from 0 through $particles {
  $box-shadow: $box-shadow,
    random($width)-$width /
      2 +
      px
      random($height)-$height /
      1.2 +
      px
      hsl(random(360), 100, 50);
  $box-shadow2: $box-shadow2, 0 0 #fff;
}
@mixin keyframes($animationName) {
  @-webkit-keyframes #{$animationName} {
    @content;
  }

  @-moz-keyframes #{$animationName} {
    @content;
  }

  @-o-keyframes #{$animationName} {
    @content;
  }

  @-ms-keyframes #{$animationName} {
    @content;
  }

  @keyframes #{$animationName} {
    @content;
  }
}

@mixin animation-delay($settings) {
  -moz-animation-delay: $settings;
  -webkit-animation-delay: $settings;
  -o-animation-delay: $settings;
  -ms-animation-delay: $settings;
  animation-delay: $settings;
}

@mixin animation-duration($settings) {
  -moz-animation-duration: $settings;
  -webkit-animation-duration: $settings;
  -o-animation-duration: $settings;
  -ms-animation-duration: $settings;
  animation-duration: $settings;
}

@mixin animation($settings) {
  -moz-animation: $settings;
  -webkit-animation: $settings;
  -o-animation: $settings;
  -ms-animation: $settings;
  animation: $settings;
}

@mixin transform($settings) {
  transform: $settings;
  -moz-transform: $settings;
  -webkit-transform: $settings;
  -o-transform: $settings;
  -ms-transform: $settings;
}

.pyro > .before,
.pyro > .after {
  position: absolute;

  width: 5px;
  height: 5px;
  border-radius: 50%;
  box-shadow: $box-shadow2;
  @include animation(
    (
      1s bang ease-out infinite backwards,
      1s gravity ease-in infinite backwards,
      5s position linear infinite backwards
    )
  );
}

.pyro > .after {
  @include animation-delay((1.25s, 1.25s, 1.25s));
  @include animation-duration((1.25s, 1.25s, 6.25s));
}

@include keyframes(bang) {
  to {
    box-shadow: $box-shadow;
  }
}

@include keyframes(gravity) {
  to {
    @include transform(translateY(200px));
    opacity: 0;
  }
}

@include keyframes(position) {
  0%,
  19.9% {
    margin-top: 10%;
    margin-left: 40%;
  }
  20%,
  39.9% {
    margin-top: 40%;
    margin-left: 30%;
  }
  40%,
  59.9% {
    margin-top: 20%;
    margin-left: 70%;
  }
  60%,
  79.9% {
    margin-top: 30%;
    margin-left: 20%;
  }
  80%,
  99.9% {
    margin-top: 30%;
    margin-left: 80%;
  }
}
</style>
