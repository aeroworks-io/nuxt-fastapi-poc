<template>
  <v-layout>
    <v-flex class="text-center">
      <img src="/v.png" alt="Vuetify.js" class="mb-5" />
      <blockquote class="blockquote">
        &#8220;{{ message }}&#8221;
        <footer>
          <small>
            <em>&mdash;{{ author }}</em>
          </small>
        </footer>
      </blockquote>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'

@Component({
  asyncData(ctx) {
    return ctx.$api.randomQuoteQuoteGet().then(response => response.data)
  },
})
export default class Inspire extends Vue {
  message!: string
  author!: string
}
</script>
