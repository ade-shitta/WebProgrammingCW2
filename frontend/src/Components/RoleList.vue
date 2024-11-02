<template>
  <div class="mt-3">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3>Character Roles</h3>
      <button class="btn btn-primary" @click="showAddModal">Add New Role</button>
    </div>

    <RoleTable 
      :roles="roles"
      @edit="editRole"
      @delete="deleteRole"
    />

    <!-- Add/Edit Modal -->
    <div class="modal fade" id="roleModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit' : 'Add' }} Role</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label class="form-label">Character</label>
                <select class="form-select" v-model="form.character_id" required>
                  <option v-for="char in characters" :key="char.id" :value="char.id">
                    {{ char.name }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Anime</label>
                <select class="form-select" v-model="form.anime_id" required>
                  <option v-for="anime in animes" :key="anime.id" :value="anime.id">
                    {{ anime.title }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Role</label>
                <select class="form-select" v-model="form.role" required>
                  <option value="MC">Main Character</option>
                  <option value="SC">Supporting Character</option>
                  <option value="ANT">Antagonist</option>
                  <option value="GC">Guest Character</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">First Appearance (Episode)</label>
                <input type="number" class="form-control" v-model="form.appearance_episode" required min="1">
              </div>
              <div class="text-end">
                <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal">Cancel</button>
                <button type="submit" class="btn btn-primary">Save</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap'
import { inject, onMounted } from 'vue'
import RoleTable from './RoleTable.vue'

export default {
  components: {
    RoleTable
  },
  setup() {
    const registerRefresh = inject('refreshRoles')
    return { registerRefresh }
  },
  mounted() {
    this.fetchRoles()
    this.fetchCharacters()
    this.fetchAnimes()
    this.modal = new Modal(document.getElementById('roleModal'))
    this.registerRefresh(() => {
      this.fetchRoles()
      this.fetchCharacters()
      this.fetchAnimes()
    })
  },
  data() {
    return {
      roles: [],
      characters: [],
      animes: [],
      isEditing: false,
      currentId: null,
      modal: null,
      form: {
        character_id: '',
        anime_id: '',
        role: 'MC',
        appearance_episode: 1
      }
    }
  },
  methods: {
    async fetchRoles() {
      const response = await fetch('http://localhost:8000/api/role/')
      const data = await response.json()
      this.roles = data.roles
    },
    async fetchCharacters() {
      const response = await fetch('http://localhost:8000/api/character/')
      const data = await response.json()
      this.characters = data.characters
    },
    async fetchAnimes() {
      const response = await fetch('http://localhost:8000/api/anime/')
      const data = await response.json()
      this.animes = data.animes
    },
    showAddModal() {
      this.isEditing = false
      this.resetForm()
      this.modal.show()
    },
    editRole(role) {
      this.isEditing = true
      this.currentId = role.id
      this.form = {
        character_id: role.character.id,
        anime_id: role.anime.id,
        role: role.role,
        appearance_episode: role.appearance_episode
      }
      this.modal.show()
    },
    resetForm() {
      this.form = {
        character_id: '',
        anime_id: '',
        role: 'MC',
        appearance_episode: 1
      }
    },
    async submitForm() {
      const url = this.isEditing 
        ? `http://localhost:8000/api/role/${this.currentId}/`
        : 'http://localhost:8000/api/role/'
      
      const response = await fetch(url, {
        method: this.isEditing ? 'PUT' : 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.form)
      })

      if (response.ok) {
        this.modal.hide()
        this.fetchRoles()
        this.resetForm()
      }
    },
    async deleteRole(id) {
      if (confirm('Are you sure you want to delete this role?')) {
        const response = await fetch(`http://localhost:8000/api/role/${id}/`, {
          method: 'DELETE'
        })
        if (response.ok) {
          this.fetchRoles()
        }
      }
    }
  }
}
</script>