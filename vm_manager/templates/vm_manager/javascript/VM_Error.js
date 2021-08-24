var beenClicked = false;
function delete_{{ app_name }}_{{ operating_system.capitalize }}(tag) {
    if (!beenClicked) {
        beenClicked = true;
        tag.disabled = true;
        {% with app_name|add:":delete_vm" as url_path %}
        window.location.href = "{% url url_path vm_id %}";
        {% endwith %}
    }
}
