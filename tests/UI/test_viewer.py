import allure
import pytest

import re

from pages.viewer_page import ViewerPage
from resources import static_data
from resources.static_data import BASE_URL, ACCOUNT_ID, PROJECT_ID
from steps.support_steps import post_folders, post_JPG_documents


@allure.feature("Add_comment")
@allure.epic("Actions_with_viewer")
@pytest.mark.viewer
@pytest.mark.ui
def test_add_comment(external_password, viewer_page: ViewerPage):
    '''тест проверяет добавление комментария к документу'''
    with allure.step('создаем папку'):
        folder_id = post_folders(project_id=static_data.PROJECT_ID, external_password=external_password).json()

    with allure.step('загружаем в папку документ JPG'):
        doc_id = post_JPG_documents(folder_id=folder_id, external_password=external_password).json()

    viewer_page.change_role_to_('project_admin')
    viewer_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation?folderId={folder_id}&viewerId={doc_id}')
    viewer_page.check_viewer_page_elements()
    viewer_page.add_comment()
    viewer_page.check_comment_is_added()


@allure.feature("Change_scale")
@allure.epic("Actions_with_viewer")
@pytest.mark.viewer
@pytest.mark.ui
def test_reduce_and_increace_scale(external_password, viewer_page: ViewerPage):
    '''тест проверяет изменение масштаба документа'''
    with allure.step('создаем папку'):
        folder_id = post_folders(project_id=static_data.PROJECT_ID, external_password=external_password).json()

    with allure.step('загружаем в папку документ JPG'):
        doc_id = post_JPG_documents(folder_id=folder_id, external_password=external_password).json()

    viewer_page.change_role_to_('project_admin')
    viewer_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation?folderId={folder_id}&viewerId={doc_id}')
    viewer_page.check_viewer_page_elements()
    viewer_page.page.wait_for_timeout(5000)
    default_scale = int(viewer_page.scale_percents.text_content().strip('%'))

    viewer_page.click_button_zoom_in()
    viewer_page.page.wait_for_timeout(1000)
    new_scale = int(viewer_page.scale_percents.text_content().strip('%'))
    assert new_scale > default_scale

    viewer_page.click_button_zoom_out()
    viewer_page.page.wait_for_timeout(1000)
    viewer_page.click_button_zoom_out()
    viewer_page.page.wait_for_timeout(1000)
    new_scale = int(viewer_page.scale_percents.text_content().strip('%'))
    assert new_scale < default_scale


@allure.feature("Change_scale")
@allure.epic("Actions_with_viewer")
@pytest.mark.viewer
@pytest.mark.ui
def test_button_by_page_size(external_password, viewer_page: ViewerPage):
    '''тест проверяет изменение масштаба документа'''
    with allure.step('создаем папку'):
        folder_id = post_folders(project_id=static_data.PROJECT_ID, external_password=external_password).json()

    with allure.step('загружаем в папку документ JPG'):
        doc_id = post_JPG_documents(folder_id=folder_id, external_password=external_password).json()

    viewer_page.change_role_to_('project_admin')
    viewer_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation?folderId={folder_id}&viewerId={doc_id}')
    viewer_page.check_viewer_page_elements()
    viewer_page.page.wait_for_timeout(5000)
    default_scale = int(viewer_page.scale_percents.text_content().strip('%'))

    viewer_page.click_button_zoom_in()
    viewer_page.page.wait_for_timeout(1000)
    new_scale = int(viewer_page.scale_percents.text_content().strip('%'))
    assert new_scale > default_scale

    viewer_page.click_button_by_page_size()
    viewer_page.page.wait_for_timeout(2000)
    new_scale = int(viewer_page.scale_percents.text_content().strip('%'))
    assert new_scale == default_scale


@allure.feature("Rotate_image")
@allure.epic("Actions_with_viewer")
@pytest.mark.viewer
@pytest.mark.ui
def test_rotate_image(external_password, viewer_page: ViewerPage):
    '''тест проверяет поворот документа'''
    with allure.step('создаем папку'):
        folder_id = post_folders(project_id=static_data.PROJECT_ID, external_password=external_password).json()

    with allure.step('загружаем в папку документ JPG'):
        doc_id = post_JPG_documents(folder_id=folder_id, external_password=external_password).json()

    viewer_page.change_role_to_('project_admin')
    viewer_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation?folderId={folder_id}&viewerId={doc_id}')
    viewer_page.check_viewer_page_elements()
    # ждем, пока изображение впишется в экран
    viewer_page.page.wait_for_timeout(5000)

    attribute_value = viewer_page.get_attribute_of_element_by_locator(viewer_page.pdf_viewer, 'style')
    pattern = r'(?P<width>\d+\.?\d*)px;.*?height:\s*(?P<height>\d+\.?\d*)px;'

    # приведение к float и обратно в str нужно, потому что фронт округляет значения
    def get_width_and_height(pattern: str, string_for_search: str) -> dict:
        m = re.search(pattern, string_for_search)

        if m:
            str_width = m.group('width')
            str_height = m.group('height')
            width = round(float(str_width), 1)
            height = round(float(str_height), 1)
            if str(width).endswith('0'):
                width = int(width)
            if str(height).endswith('0'):
                height = int(height)
            return {
                "width": str(width),
                "height": str(height)
            }
        raise Exception('в атрибуте не найдены значения для длины и ширины элемента')
    
    # альтернативный способ получить размеры элемента: box = viewer_page.pdf_viewer.bounding_box()
    sides = get_width_and_height(pattern=pattern, string_for_search=attribute_value)
    default_width = sides['width']
    default_height = sides['height']
     
    # 1st click - the image is rotated 90 degrees counterclockwise
    viewer_page.click_button_turn()
    viewer_page.check_element_has_attribute_with_value(
                some_locator=viewer_page.pdf_viewer,
                attribute_name='style',
                attribute_value=f'width: {default_height}px; height: {default_width}px;')
    
    # 2nd click - the image is rotated 180 degrees
    viewer_page.click_button_turn()
    viewer_page.check_element_has_attribute_with_value(
                some_locator=viewer_page.pdf_viewer,
                attribute_name='style',
                attribute_value=f'width: {default_width}px; height: {default_height}px;')
    
    # 3rd click - the image is rotated 270 degrees counterclockwise
    viewer_page.click_button_turn()
    viewer_page.check_element_has_attribute_with_value(
                some_locator=viewer_page.pdf_viewer,
                attribute_name='style',
                attribute_value=f'width: {default_height}px; height: {default_width}px;')
    
    # 4th click - the image is rotated 360 degrees
    viewer_page.click_button_turn()
    viewer_page.check_element_has_attribute_with_value(
                some_locator=viewer_page.pdf_viewer,
                attribute_name='style',
                attribute_value=f'width: {default_width}px; height: {default_height}px;')
