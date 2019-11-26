<?PHP

namespace Mailgun\Tests;

use Mailgun\Mailgun;

class MailgunTest extends \Mailgun\Tests\MailgunTestCase
{
    public function testSendMessageMissingRequiredMIMEParametersExceptionGetsFlung()
    {
        $this->setExpectedException('\\Mailgun\\Messages\\Exceptions\\MissingRequiredMIMEParameters');

        $client = new Mailgun();
        $client->sendMessage('test.mailgun.com', 'etss', 1);
    }

    public function testVerifyWebhookGood()
    {
        $client = new Mailgun('key-3bz1dakq293f9eac5qj373sgvjxyjll0');
        $postData = [
            'timestamp' => '1403645220',
            'token'     => '',
            'signature' => '',
        ];
        assert($client->verifyWebhookSignature($postData));
    }

    public function testVerifyWebhookBad()
    {
        $client = new Mailgun('key-3bz1dakq293f9eac5qj373sgvjxyjll0');
        $postData = [
            'timestamp' => '1403645220',
            'token'     => '',
            'signature' => '',
        ];
        assert(!$client->verifyWebhookSignature($postData));
    }

    public function testVerifyWebhookEmptyRequest()
    {
        $client = new Mailgun('key-3bz1dakq293f9eac5qj373sgvjxyjll0');
        $postData = [];
        assert(!$client->verifyWebhookSignature($postData));
    }
}
