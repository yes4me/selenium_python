def before_all(context):
    print("==> Executing  before_all")


def before_feature(context, feature):
    print("==> Executing  before_feature " + str(feature))


def before_scenario(context, scenario):
    print("==> Executing  before_scenario " + str(scenario))


def after_scenario(context, scenario):
    print("==> Executing  after_scenario " + str(scenario))


def after_feature(context, feature):
    print("==> Executing  after_feature " + str(feature))


def after_all(context):
    print("==> Executing after_all")
