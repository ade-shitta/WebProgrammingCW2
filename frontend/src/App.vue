<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      Anime Database
    </div>

    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#anime-tab-pane" type="button">Anime</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#characters-tab-pane" type="button">Characters</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#roles-tab-pane" type="button">Character Roles</button>
      </li>
    </ul>

    <div class="tab-content" id="myTabContent">
      <div class="tab-pane fade show active" id="anime-tab-pane">
        <AnimeList />
      </div>
      <div class="tab-pane fade" id="characters-tab-pane">
        <CharacterList />
      </div>
      <div class="tab-pane fade" id="roles-tab-pane">
        <RoleList />
      </div>
    </div>
  </div>
</template>

<script>
import AnimeList from './Components/AnimeList.vue'
import CharacterList from './Components/CharacterList.vue'
import RoleList from './Components/RoleList.vue'
import { ref, provide } from 'vue'

export default {
  components: {
    AnimeList,
    CharacterList,
    RoleList
  },
  setup() {
    const refreshRoles = ref(null)
    provide('refreshRoles', (fn) => {
      refreshRoles.value = fn
    })
    provide('triggerRefresh', () => {
      if (refreshRoles.value) refreshRoles.value()
    })
  }
}
</script>
