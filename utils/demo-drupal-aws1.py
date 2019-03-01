from screenshot_archiver import WebsiteScreenshotArchiver
import time

class DemoDrupal(WebsiteScreenshotArchiver):
  def browse_site(self):
    self.navigateTo("https://govready.signin.aws.amazon.com/console")
    time.sleep(18)
    self.navigateTo("https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:sort=instanceId")
    time.sleep(4)
    self.screenshot("aws-instance")
    # Security groups
    self.navigateTo("https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#SecurityGroups:groupId=sg-0897ed9775ba2a5bf;sort=groupId")
    time.sleep(4)
    self.screenshot("aws-security-group-description")

    self.click_element('.GFRVLNABDNB div:nth-child(3) .gwt-Image') # maximize the panel
    time.sleep(1)

    self.click_element('.gwt-TabLayoutPanelTab:nth-child(2)') # Inbound
    time.sleep(1)
    self.screenshot("aws-security-group-inbound")

    self.click_element('.gwt-TabLayoutPanelTab:nth-child(3)') # Outbound
    time.sleep(1)
    self.screenshot("aws-security-group-outbound")
    
    # self.fill_field("#search_form_input_homepage", "GovReady")
    # self.click_with_screenshot("#search_button_homepage", "search1")

if __name__ == "__main__":
  DemoDrupal().__main__()
