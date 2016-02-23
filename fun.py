import urllib2
import logging
import StringIO
import csv

base_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris"

default_agent = 'Mozilla/5.0 ' \
                '(X11; Ubuntu; Linux x86_64; rv:37.0) ' \
                'Gecko/20100101 Firefox/37.0'

def bind(x, *fs):
    if x:
        if len(fs) > 0:
            f  = fs[0]
            fs = fs[1:]
            return bind(f(x), *fs)
        else:
            return x
    else:
        logger = logging.getLogger(__name__)
        logger.error('Unable to run {:s}'.format(f.func_name))
        return x


def download(name):
    logger = logging.getLogger(__name__)

    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent',
                          default_agent)]

    url = '{:s}/{:s}'.format(base_url, name)
    print url

    try:
        response = opener.open(url, timeout=5)
        html_data = response.read()
    except:
        logger.error('Unable to get {:s}'.format(name))
        html_data = None

    return html_data


def de_cvs(data):
    sdata = StringIO.StringIO(data)
    reader = csv.reader(sdata, delimiter=',')

    return [ row for row in reader if len(row) > 0 ]


def decode_attributes(data):
    """
    Attribute Information:
    1. sepal length in cm
    2. sepal width in cm
    3. petal length in cm
    4. petal width in cm
    5. class
    """
    return [ {'septal_length': float(a),
              'septal_width': float(b),
              'petal_length': float(c),
              'petal_width': float(d),
              'class': e }
            for (a, b, c, d, e) in data ]


def main():
    data = bind('iris.data', download, de_cvs, decode_attributes)


if __name__ == '__main__':
    main()
