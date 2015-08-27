from teuthology.config import config


class TestOpenStack(object):

    def test_config_user_data(self):
        os_type = 'rhel'
        os_version = '7.0'
        openstack_config = config['openstack']
        template_path = openstack_config['user-data'].format(
            os_type=os_type,
            os_version=os_version)
        assert os_type in template_path
        assert os_version in template_path
