 #  Unless required by applicable law or agreed to in writing, software
 #  distributed under the License is distributed on an "AS IS" BASIS,
 #  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 #  See the License for the specific language governing permissions and
 #  limitations under the License.
 #
 #  Copyright 2023 mrpaw69

from datetime import datetime

date_format = '%d/%m/%y %H:%M:%S'

def to_timestamp(str_time):
	return datetime.strptime(str_time, date_format).timestamp()

def time_to_string(t):
	return t.strftime('%B %d, %A, at %H:%M')

def time_from_utc(seconds):
	return datetime.utcfromtimestamp(seconds)