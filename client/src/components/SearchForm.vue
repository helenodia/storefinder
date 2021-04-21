<template>
  <div>
    <section class="search-form__section">
      <div class="search-form__heading">
        <h1 class="heading">Find a store</h1>
      </div>
      <form class="search-form__form"
            method="get"
            action="/stores"
            id="search-form"
            role="search">

        <div class="search-form__container--item">
          <label class="search-form__label"
                 for="search">
            Enter a town, city or postcode to find nearby stores:
          </label>

          <input class="search-form__input"
                 id="search"
                 name="search"
                 type="search"
                 aria-label="Search for a store"
                 maxlength="35"
                 minlength="2"
                 v-model.trim.lazy="query">
        </div>

        <div class="search-form__container--item">
          <div class="search-form__container--btn">
            <button class="search-form__btn--primary"
                    type="submit"
                    @click.prevent="fetchStores">
              Search
            </button>
          </div>
        </div>
      </form>
    </section>
  </div>
  <SearchResults v-show="isSubmitted"
                 v-bind:stores="stores"
                 v-bind:query="query" />
</template>

<script>
import axios from 'axios';
import SearchResults from './SearchResults.vue';

export default {
  name: 'SearchForm',
  components: {
    SearchResults
  },
  data() {
    return {
      query: '',
      stores: [],
      isSubmitted: false
    }
  },
  methods: {
    async fetchStores() {
      try {
        const url = `http://localhost:5000/stores?q=${this.query}`
        const response = await axios.get(url)
        const stores = response.data
        this.stores = stores.map(store => ({
          name: store.name,
          postcode: store.postcode,
        }))
        this.stores = JSON.stringify(stores);
        this.stores = this.stores.replace(/[_-]/g, " ");
        this.stores = JSON.parse(this.stores);
        // Display SearchResults section
        this.isSubmitted = true;
      } catch (err) {
        if (err.response) {
          // Client received an error response (5xx, 4xx)
          console.log("Server Error:", err)
        } else if (err.request) {
          // Client never received a response, or request never left
          console.log("Network Error:", err)
        } else {
          console.log("Client Error:", err)
        }
      }
    }
  }
}
</script>
