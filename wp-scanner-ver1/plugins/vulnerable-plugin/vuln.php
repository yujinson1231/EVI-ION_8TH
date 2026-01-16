<?php

add_action('wp_ajax_update_setting', 'update_setting');

function update_setting() {
   
    update_option('siteurl', $_POST['url']);
}
