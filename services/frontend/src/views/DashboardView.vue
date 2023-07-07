<template>
    <div>
        <section>
            <h1>Add new note</h1>
            <hr><br>
            <form @submit.prevent="submit">
                <div class="mb-3">
                    <label for="title" class="form-label">Title:</label>
                    <input type="text" name="title" v-model="form.title" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="comments" class="form-label">Comments:</label>
                    <input type="textarea" name="comments" v-model="form.comments" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="priority_level" class="form-label">Priority Level:</label>
                    <input type="int" min="1" max="5" name="priority_level" v-model="form.priority_level" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="due_date" class="form-label">Due Date:</label>
                    <input type="date" name="due_date" v-model="form.due_date" class="form-control">
                </div>
            </form>
        </section>
        <br><br>
        <section>
            
        </section>
    </div>
</template>



<script>
import { defineComponent } from 'vue';
import { mapGetters,mapActions } from 'vuex';

export default defineComponent({
    name:'Dashboard',
    data(){
        return{
            form:{
                title:'',
                comments:'',
                priority_level:0,
                due_date: new Date(),
            },
        };
    },
    created: function(){
        return this.$store.dispatch('getTasks');
    },
    computed:{
        ...mapGetters({tasks: 'stateTasks'}),
    },
    methods:{
        ...mapActions(['createTask']),
        async submit(){
            await this.createTask(this.form);
        },
    },
});

</script>