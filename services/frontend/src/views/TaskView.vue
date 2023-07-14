<template>
  <div v-if="task">
    <p><strong>Title:</strong> {{ task.title }}</p>
    <p><strong>Comments:</strong> {{ task.comments }}</p>
    <p><strong>Priority Level:</strong> {{ task.priority_level }}</p>
    <p><strong>Due Date:</strong> {{ task.due_date }}</p>

    <div v-if="user.id === task.user.id">
      <p>
        <router-link :to="{ name: 'EditTask', params: { id: task.id } }" class="btn btn-primary"
          >Edit</router-link
        >
      </p>
      <p><button @click="removeTask()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";
import { Suspense } from "vue";

export default defineComponent({
  name: "Task",
  props: ["id"],
  data() {
    return {
      taskid: `${this.$route.params.id}`,
    };
  },
  async created() {
    console.log(`${this.taskid}`);
    await this.viewTask(this.taskid).catch((e) => console.error(e));
  },
  computed: {
    // and then here it grabs that task from the store
    ...mapGetters({ task: "stateTask", user: "stateUser" }),
  },
  methods: {
    ...mapActions(["viewTask", "deleteTask"]),
    async removeTask() {
      try {
        await this.deleteTask(this.id);
        this.$router.push("/dashboard");
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>
